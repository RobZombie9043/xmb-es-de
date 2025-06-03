@echo off
REM Custom event script for ES-DE: Runs on application startup

REM Change to the script directory (this batch file's directory)
cd /d "%~dp0"
if errorlevel 1 (
    echo Failed to change directory!
    pause
    exit /b 1
)

REM Run the Python script located two levels up in themes\xmb-es-de
python "..\..\themes\xmb-es-de\seteup\generate_xml.py"