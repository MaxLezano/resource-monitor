import serial
import os

def read_config(path):
    result = {}
    if not os.path.exists(path):
        port = input("Enter the port number (e.g., 6 for COM6): ")
        baud_rate = "9600"
        change_baud = input("The default value for BAUD_RATE is 9600. Do you want to change it? (y/n): ").strip().lower()
        if change_baud == "y":
            baud_rate = input("Enter the new BAUD_RATE: ") or "9600"
        result['PORT'] = f'COM{port}'
        result['BAUD_RATE'] = baud_rate
        with open(path, 'w') as f:
            f.write(f'PORT=COM{port}\n')
            f.write(f'BAUD_RATE={baud_rate}\n')
    else:
        with open(path, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    result[key] = value
    return result

config_path = os.path.join(os.path.dirname(__file__), 'config.txt')
config = read_config(config_path)

PORT = config.get('PORT', 'COM6')
BAUD_RATE = int(config.get('BAUD_RATE', '9600'))

ser = serial.Serial(PORT, BAUD_RATE)

def send_command(command):
    fin = bytes([0xFF, 0xFF, 0xFF])
    ser.write(command.encode('utf-8') + fin)