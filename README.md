# SCT_CS_4
# 🛡️ Keylogger with Flask GUI & Screenshot Logging

A Python-based keylogger tool for educational and monitoring purposes. It records keystrokes, captures screenshots on window changes, saves logs in CSV format, and provides a simple Flask GUI to view all logs.


## 📦 Features

- 🔑 Logs all keystrokes
- 📸 Captures screenshots when active window changes
- 🧾 Saves logs to CSV file (`keylogs.csv`)
- 🌐 Flask-based web interface to view:
  - Keystroke logs
  - Timestamps
  - Active window names
  - Captured screenshots

---

## 🚀 Installation

1. Clone or download this project:
   ``bash
   git clone https://github.com/your-username/keylogger_project.git
   cd keylogger_project
`
2. Set up a virtual environment (recommended):

   ``bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:

   ``bash
   pip install -r requirements.txt
   ```

> ⚠️ Tested on **Kali Linux**, Python 3.13+

---

## ⚙️ Usage

### 1. Run the keylogger:

``bash
python keylogger_gui.py
```

```
* Logs are saved in `keylogs.csv`
* Screenshots are saved inside the `screenshots/` directory
```

```
### 2. Access the Web GUI

Once running, open your browser and go to:

```
http://127.0.0.1:5000
```

You can view:

* All recorded logs
* Associated screenshots
* Download the logs in CSV format

---

## 🧾 Log Format (CSV)

Each row includes:

| Timestamp           | Key Pressed | Active Window | Screenshot Filename        |
| ------------------- | ----------- | ------------- | -------------------------- |
| 2025-05-18 08:30:12 | A           | Text Editor   | 20250518\_083012\_Text.png |

---

## 📁 Project Structure

``
keylogger_project/
├── keylogger_gui.py       # Main script
├── keylogs.csv            # Logs (auto-created)
├── secret.key             # Optional (if encryption used)
├── screenshots/           # Screenshot images
└── templates/             # HTML for Flask GUI (auto-handled)
```

```

## 🛑 Disclaimer

This tool is intended **for ethical, educational, or authorized monitoring use only**. Misuse of keyloggers is **illegal** and strictly discouraged.

---

## 🧠 Author

Made with ❤️ by Akanksha (for educational & project purposes)

```
