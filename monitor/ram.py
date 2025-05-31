import subprocess
from .hardware import computer

def get_ram_usage():
    used_percent = 0.0
    used_gb = 0.0

    for hw in computer.Hardware:
        if hw.HardwareType == hw.HardwareType.RAM:
            hw.Update()
            for sensor in hw.Sensors:
                if sensor.SensorType == sensor.SensorType.Load and sensor.Name == "Memory":
                    used_percent = sensor.Value
                elif sensor.SensorType == sensor.SensorType.Data and "Used Memory" in sensor.Name:
                    used_gb = sensor.Value
            break

    return used_percent, used_gb

def get_ram_frequency():
    for hw in computer.Hardware:
        if hw.HardwareType == hw.HardwareType.RAM:
            hw.Update()
            for sensor in hw.Sensors:
                if sensor.SensorType == sensor.SensorType.Clock:
                    if "Memory" in sensor.Name or "RAM" in sensor.Name:
                        return int(sensor.Value)

    try:
        output = subprocess.check_output("wmic memorychip get speed", shell=True).decode()
        lines = output.strip().split("\n")
        speeds = [int(line.strip()) for line in lines[1:] if line.strip().isdigit()]
        if speeds:
            return max(speeds)
    except Exception as e:
        print("Error getting RAM frequency with WMIC:", e)

    return 0
