@echo off
title Fast Stream Clipper Launcher
echo === Stream Clipper Initialization (Windows) ===
echo.

:: 1. Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [X] ERROR: Python is not installed.
    echo Please open the Microsoft Store, search for "Python", and install it.
    pause
    exit /b
)

:: 2. Check for FFmpeg
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] FFmpeg is missing. Installing via Windows Package Manager (winget)...
    winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
    echo.
    echo [!] FFmpeg installed! Please close this window and run the script again.
    pause
    exit /b
) else (
    echo [+] FFmpeg found.
)

:: 3. Setup Python Virtual Environment
set VENV_DIR=clipper_env
if not exist %VENV_DIR% (
    echo [*] Creating new Python virtual environment...
    python -m venv %VENV_DIR%
)

:: 4. Activate Venv and Install Pip Packages
echo [*] Activating environment and checking Python dependencies...
call %VENV_DIR%\Scripts\activate.bat

python -m pip install --upgrade pip -q
pip install yt-dlp opencv-python pytesseract -q

echo [+] Environment ready!
echo === Launching App ===
echo.

:: 5. Launch the GUI silently
pythonw clipper_gui.py

if %errorlevel% neq 0 (
    echo.
    echo [X] The application crashed. See the errors above.
    pause
)
