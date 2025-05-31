import serial

puerto = "COM6"
baudrate = 9600
ser = serial.Serial(puerto, baudrate)

def send_command(comando):
    fin = bytes([0xFF, 0xFF, 0xFF])
    ser.write(comando.encode('utf-8') + fin)
