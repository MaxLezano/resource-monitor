# Hardware Monitor & Audio Controller

Python application to monitor hardware (CPU, GPU, RAM) and control system audio from an external interface (e.g., a Nextion display connected via serial port).

## Requirements

- Windows 10/11
- Python 3.12
- Python dependencies: see `Pipfile`
- Additional files (in the `libs/` folder):
  - [`nircmd.exe`](https://www.nirsoft.net/utils/nircmd.html)
  - [`OpenHardwareMonitorLib.dll`](https://github.com/openhardwaremonitor/openhardwaremonitor/releases)
  - `OpenHardwareMonitorLib.sys`

## Installation

1. Clone this repository or download the source code.
2. Install project dependencies using `pipenv`:
   ```sh
   pip install pipenv
   pipenv install
   pipenv shell
   ```
3. Ensure the required files are present in the `libs/` folder:
   - Download `nircmd.exe` and place it in `libs/`
   - Download `OpenHardwareMonitorLib.dll` and place it in `libs/`
   - Ensure `OpenHardwareMonitorLib.sys` is also in `libs/`
4. Connect your Nextion display (or other serial device) to the port configured in `monitor/serial_comm.py`.

## Usage

- To run in development mode:
  ```sh
  python core/debug.py
  ```
- To build a portable executable:
  ```sh
  ./build_exe.bat
  ```
  The executable will be located in the `release/` folder.

## Project Structure

- `core/` — Main logic and event handling
- `monitor/` — Hardware monitoring and serial communication
- `audio/` — Audio control
- `ui/` — Interface/page management
- `libs/` — External libraries and utilities
- `build_exe.bat` — Script to build the executable
- `.gitignore` — Files/folders ignored by git

## Notes

- Change the serial port in `monitor/serial_comm.py` if needed.
- The device names used in configuration files must match the names configured on your system.
- Adjust configuration files as needed for your setup.
- Some functions may require administrator privileges to work correctly.

---

This project is modular and can be adapted to different interfaces or input/output devices.
