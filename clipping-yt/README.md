#  Fast Stream Clipper Pro

A lightweight, automated desktop application designed to instantly slice highlights from massive VODs and local video files. It bypasses heavy video editors like Premiere Pro by utilizing `ffmpeg` for instantaneous, zero-encoding cuts, and `yt-dlp` to download specific timestamps directly from YouTube servers.

##  Key Features
* **Zero-Re-encoding Slicing:** Cuts local video files in milliseconds without re-rendering pixels.
* **Direct Cloud Clipping:** Extracts specific timestamps from YouTube URLs without downloading the entire 4-hour stream.
* **Batch Processing Queue:** Queue up multiple highlights and walk away while the engine processes them all automatically.
* **Smart Bandwidth Saver:** Option to download a full stream once, then perform instant local cuts for all subsequent clips in the queue.
* **Cross-Platform:** Includes automated environment launchers for both Windows (`.bat`) and Linux (`.sh`).

---

## How to Run the App

You do not need to manually install Python packages or touch the command line. The provided launcher scripts will automatically check your system, install required tools (like `ffmpeg`), build an isolated virtual environment, and launch the GUI.

### **For Windows Users:**
1. Ensure you have **Python 3** installed from the Microsoft Store or python.org (ensure "Add to PATH" is checked during install).
2. Place `clipper_gui.py` and `start_clipper.bat` in the same folder.
3. **Double-click `start_clipper.bat`**.
   * *Note: On the first run, a black window will appear as it installs FFmpeg and sets up the environment. Subsequent launches will be near-instant.*

### **For Linux Users:**
1. Place `clipper_gui.py` and `start_clipper.sh` in the same folder.
2. Open your terminal in that folder and make the script executable:
   ```bash
   chmod +x start_clipper.sh
   ```
3. Run the launcher:
   ```bash
   ./start_clipper.sh
   ```
   * *Note: It may prompt for your `sudo` password to install `ffmpeg` via your package manager on the first run.*

---

## Advanced Automation Plugins (Optional)

The application includes an expandable architecture for automated clipping (e.g., finding spikes in audio, scanning chat logs, or reading on-screen text like "YOU DIED"). 

**To use the OCR (Optical Character Recognition) Vision scanner:**
1. You must install the core Tesseract engine on your operating system.
   * **Windows:** Download the installer from UB-Mannheim.
   * **Linux:** Run `sudo apt install tesseract-ocr`.
2. Open `clipper_gui.py` in a text editor and add your specific OpenCV and Tesseract logic into the designated placeholder blocks within the `run_engine` function.

---

## Troubleshooting

* **"Python is not recognized" (Windows):** You need to install Python. If it is already installed, reinstall it and ensure the checkbox **"Add Python to PATH"** is selected at the bottom of the installer window.
* **"App crashes immediately after opening":** Run the launcher script from inside a terminal (Command Prompt or Bash) instead of double-clicking it. This will keep the window open so you can read the specific error message.
```
