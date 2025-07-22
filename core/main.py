from monitor.serial_comm import send_command
from monitor.cpu import get_cpu_name
from monitor.gpu import get_gpu_name
from monitor.ram import get_ram_frequency

def main():
    send_command(f'cpuName.txt="{get_cpu_name()}"')
    send_command(f'gpuName.txt="{get_gpu_name()}"')
    send_command(f'ramFrequency.txt="{get_ram_frequency()} MHz"')
    print("Build entry point executed successfully.")

if __name__ == "__main__":
    main()