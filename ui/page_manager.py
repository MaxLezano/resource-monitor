from monitor.serial_comm import ser, send_command

PAGES = ["Home", "Audio"]
current_page_index = 0

def change_page(direction):
    global current_page_index
    if direction == "next":
        current_page_index = (current_page_index + 1) % len(PAGES)
    elif direction == "prev":
        current_page_index = (current_page_index - 1) % len(PAGES)
    send_command(f'page {PAGES[current_page_index]}')

def listen_for_events(callback):
    while True:
        if ser.in_waiting:
            data = ser.read_until(b'\xFF\xFF\xFF')
            if not data or data[0] != 0x65 or len(data) < 4:
                continue
            page_id = data[1]
            com_id = data[2]
            event = data[3]
            callback(page_id, com_id, event)