@echo off
set /p PORT_NUM=Enter the port number (e.g., 6 for COM6):
set PORT=COM%PORT_NUM%

set BAUD_RATE=9600
set /p CHANGE_BAUD=The default value for BAUD_RATE is 9600. Do you want to change it? (y/n):
if /I "%CHANGE_BAUD%"=="y" (
    set /p BAUD_RATE=Enter the new BAUD_RATE:
)

echo Selected port: %PORT%
echo Baud rate: %BAUD_RATE%

echo ================================
echo [*] Activating virtual environment...
echo ================================
REM If you use venv, activate it here. Otherwise, skip this line.
REM call venv\Scripts\activate

echo ================================
echo [*] Building executable with PyInstaller...
echo ================================
pyinstaller --noconfirm --clean --onefile ^
  --add-data "libs\OpenHardwareMonitorLib.dll;libs" ^
  --add-data "libs\OpenHardwareMonitorLib.sys;libs" ^
  --add-data "libs\nircmd.exe;libs" ^
  --add-data "monitor;monitor" ^
  --add-data "audio;audio" ^
  --add-data "ui;ui" ^
  --add-data "libs\default_volume_levels.json;libs" ^
  core\main.py --name main

echo.
echo ================================
echo [*] Creating portable folder...
echo ================================

REM Create release folder if it doesn't exist
if not exist release mkdir release
if exist release\libs rmdir /s /q release\libs
mkdir release\libs

REM Check if the dist folder exists and contains the executable
if not exist dist\main.exe (
    echo [X] ERROR: dist\main.exe not found. The compilation failed.
    pause
    exit /b 1
)

REM Copy executable
copy dist\main.exe release\main.exe

REM Copy required files
copy libs\OpenHardwareMonitorLib.dll release\libs\
copy libs\OpenHardwareMonitorLib.sys release\libs\
copy libs\nircmd.exe release\libs\
copy libs\default_volume_levels.json release\libs\

REM Remove dist folder to avoid duplicates
if exist dist rmdir /s /q dist

echo.
echo ================================
echo [*] Cleaning build folder...
echo ================================
REM Remove build folder to keep project clean
if exist build rmdir /s /q build

echo.
echo ================================
echo [✔] Build complete. The executable is in the /release folder
echo ================================
pause