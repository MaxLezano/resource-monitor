import clr
import os

dll_path = os.path.abspath(os.path.join("libs", "OpenHardwareMonitorLib.dll"))
clr.AddReference(dll_path)

from OpenHardwareMonitor import Hardware

computer = Hardware.Computer()
computer.CPUEnabled = True
computer.GPUEnabled = True
computer.RAMEnabled = True
computer.Open()
