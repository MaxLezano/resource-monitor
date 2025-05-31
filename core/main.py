import time
import threading
from core.event_handler import handle_event
from monitor.cpu import get_cpu_temp, get_cpu_load, get_cpu_name
from monitor.gpu import get_gpu_temp_and_load, get_gpu_name
from monitor.ram import get_ram_usage, get_ram_frequency
from monitor.serial_comm import send_command
from ui.page_manager import listen_for_events

def update_monitor_data():
    while True:
        cpu_temp = get_cpu_temp()
        cpu_load = get_cpu_load()
        gpu_temp, gpu_load = get_gpu_temp_and_load()
        ram_load, ram_used_gb = get_ram_usage()

        send_command(f'cpuTemp.txt="{cpu_temp:.1f}°C"' if cpu_temp is not None else 'cpuTemp.txt="N/A"')
        send_command(f'gpuTemp.txt="{gpu_temp:.1f}°C"' if gpu_temp is not None else 'gpuTemp.txt="N/A"')
        send_command(f'ramUsage.txt="{ram_used_gb:.1f} GB"')
        send_command(f'cpuLoad.val={int(cpu_load)}')
        send_command(f'gpuLoad.val={int(gpu_load)}')
        send_command(f'ramLoad.val={int(ram_load)}')
        time.sleep(2)

def send_initial_info():
    send_command(f'cpuName.txt="{get_cpu_name()}"')
    send_command(f'gpuName.txt="{get_gpu_name()}"')
    send_command(f'ramFrequency.txt="{get_ram_frequency()} MHz"')

def main():
    send_initial_info()
    threading.Thread(target=update_monitor_data, daemon=True).start()
    threading.Thread(target=listen_for_events, args=(handle_event,), daemon=True).start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()