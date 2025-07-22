import os
from dotenv import load_dotenv
import serial

load_dotenv()

PORT = os.getenv("PORT")
BAUD_RATE = int(os.getenv("BAUD_RATE"))
ser = serial.Serial(PORT, BAUD_RATE)

def send_command(comando):
    fin = bytes([0xFF, 0xFF, 0xFF])
    ser.write(comando.encode('utf-8') + fin)