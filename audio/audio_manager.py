import subprocess
from monitor.serial_comm import send_command, ser
import struct
import keyboard

audio_muted = False
DEVICE_MAP = {
    0: "JBL",
    1: "Barra de Sonido T&V"
}

def set_audio_muted(mute: bool):
    global audio_muted
    audio_muted = mute
    subprocess.run(["nircmd.exe", "mutesysvolume", "1" if mute else "0"])
    send_command(f"audioSwitch.val={'1' if mute else '0'}")

def toggle_audio():
    set_audio_muted(not audio_muted)

def set_volume_from_slider():
    ser.reset_input_buffer()
    send_command("get audioVolume.val")
    response = ser.read_until(b'\xFF\xFF\xFF')
    if not response or b'\x71' not in response:
        return
    try:
        idx = response.index(b'\x71')
        value_bytes = response[idx + 1:idx + 5]
        volume_value = struct.unpack('<I', value_bytes)[0]
    except Exception:
        return
    subprocess.run(["nircmd.exe", "setsysvolume", str(int(volume_value * 655.35))])
    send_command(f'audioLevel.txt="{volume_value}"')
    send_command(f'audioVolume.val={volume_value}')

def set_audio_device(audio_device):
    subprocess.run(["nircmd.exe", "setdefaultsounddevice", audio_device])

def set_device_from_selector():
    ser.reset_input_buffer()
    send_command("get deviceSelector.val")
    response = ser.read_until(b'\xFF\xFF\xFF')
    if not response or b'\x71' not in response:
        return
    try:
        idx = response.index(b'\x71')
        value_bytes = response[idx + 1:idx + 5]
        selector_value = struct.unpack('<I', value_bytes)[0]
    except Exception:
        return
    device_name = DEVICE_MAP.get(selector_value)
    if device_name:
        set_audio_device(device_name)

def send_multimedia_key(action):
    key_map = {
        "play": "play/pause media",
        "prev": "previous track",
        "next": "next track"
    }
    key = key_map.get(action)
    if key:
        keyboard.send(key)