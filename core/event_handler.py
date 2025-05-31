from audio.audio_manager import toggle_audio, set_volume_from_slider, set_device_from_selector, send_multimedia_key
from ui.page_manager import change_page

COMPONENTS = {
    (1, 4): "audioSwitch",
    (1, 6): "audioVolume",
    (1, 11): "prevPage",
    (0, 19): "nextPage",
    (1, 15): "prevBtn",
    (1, 16): "nextBtn",
    (1, 17): "deviceSelect",
    (1, 18): "playBtn"
}

def handle_event(page_id, com_id, event):
    if event != 1:
        return
    name = COMPONENTS.get((page_id, com_id))
    if name == "nextPage":
        change_page("next")
    elif name == "prevPage":
        change_page("prev")
    elif name == "audioSwitch":
        toggle_audio()
    elif name == "audioVolume":
        set_volume_from_slider()
    elif name == "deviceSelect":
        set_device_from_selector()
    elif name == "playBtn":
        send_multimedia_key("play")
    elif name == "prevBtn":
        send_multimedia_key("prev")
    elif name == "nextBtn":
        send_multimedia_key("next")