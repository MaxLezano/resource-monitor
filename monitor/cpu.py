from .hardware import computer

def get_cpu_temp():
    for hw in computer.Hardware:
        if hw.HardwareType == hw.HardwareType.CPU:
            hw.Update()
            for sensor in hw.Sensors:
                if sensor.SensorType == sensor.SensorType.Temperature:
                    if "Package" in sensor.Name:
                        return sensor.Value
    return 0.0

def get_cpu_load():
    for hw in computer.Hardware:
        if hw.HardwareType == hw.HardwareType.CPU:
            hw.Update()
            for sensor in hw.Sensors:
                if sensor.SensorType == sensor.SensorType.Load and sensor.Name == "CPU Total":
                    return sensor.Value
    return 0.0

def get_cpu_name():
    for hw in computer.Hardware:
        if hw.HardwareType == hw.HardwareType.CPU:
            return hw.Name
    return "Unknown CPU"
