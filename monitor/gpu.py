from .hardware import computer

def get_gpu_temp_and_load():
    for hw in computer.Hardware:
        if hw.HardwareType in (hw.HardwareType.GpuNvidia, hw.HardwareType.GpuAti):
            hw.Update()
            temp = None
            load = None
            for sensor in hw.Sensors:
                if sensor.SensorType == sensor.SensorType.Temperature and "Core" in sensor.Name:
                    temp = sensor.Value
                elif sensor.SensorType == sensor.SensorType.Load and "Core" in sensor.Name:
                    load = sensor.Value
            if temp is not None and load is not None:
                return temp, load
    return 0.0, 0.0

def get_gpu_name():
    for hw in computer.Hardware:
        if hw.HardwareType in (hw.HardwareType.GpuNvidia, hw.HardwareType.GpuAti):
            name = hw.Name.strip()
            if name.startswith("NVIDIA NVIDIA"):
                name = name.replace("NVIDIA NVIDIA", "NVIDIA", 1)
            elif name.startswith("AMD AMD"):
                name = name.replace("AMD AMD", "AMD", 1)
            return name
    return "No GPU"
