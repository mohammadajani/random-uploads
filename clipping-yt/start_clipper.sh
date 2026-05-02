#!/bin/bash

echo "=== Stream Clipper Initialization (Linux) ==="

# 1. Check for System Binaries
MISSING_SYS=()
if ! command -v ffmpeg &> /dev/null; then
    MISSING_SYS+=("ffmpeg")
fi

if [ ${#MISSING_SYS[@]} -ne 0 ]; then
    echo "[!] Missing required system tools: ${MISSING_SYS[*]}"
    echo "[*] Requesting permission to install them via apt..."
    sudo apt update
    sudo apt install -y "${MISSING_SYS[@]}" python3-venv
else
    echo "[+] All system binaries found."
fi

# 2. Setup Python Virtual Environment
VENV_DIR="clipper_env"

if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Creating new Python virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# 3. Activate Venv and Install Pip Packages
echo "[*] Activating environment and checking Python dependencies..."
source "$VENV_DIR/bin/activate"

pip install --upgrade pip quiet
pip install yt-dlp opencv-python pytesseract quiet

echo "[+] Environment ready!"
echo "=== Launching App ==="

# 4. Launch the GUI
python3 clipper_gui.py

# Deactivate venv when closed
deactivate
