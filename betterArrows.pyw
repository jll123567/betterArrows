from pynput import keyboard

keyList = []


# noinspection PyPep8Naming
def getKeys(key):
    global keyList
    if key == keyboard.Key.f2:
        keyList.append(key)
    else:
        if keyboard.Key.f2 in keyList:
            keyList.append(key)


# noinspection PyPep8Naming
def emptyKeys(key):
    global keyList
    if keyboard.Key.f2 in keyList:
        if keyboard.Key.right in keyList:
            keyboard.Controller().press(keyboard.Key.end)
            keyList.remove(keyboard.Key.right)
        if keyboard.Key.left in keyList:
            keyboard.Controller().press(keyboard.Key.home)
            keyList.remove(keyboard.Key.left)
        if keyboard.Key.up in keyList:
            keyboard.Controller().press(keyboard.Key.page_up)
            keyList.remove(keyboard.Key.up)
        if keyboard.Key.down in keyList:
            keyboard.Controller().press(keyboard.Key.page_down)
            keyList.remove(keyboard.Key.down)
    if key == keyboard.Key.f2:
        keyList = []


def d():
    with keyboard.Listener(on_press=getKeys, on_release=emptyKeys) as kbLstn:
        kbLstn.join()


if __name__ == "__main__":
    with keyboard.Listener(on_press=getKeys, on_release=emptyKeys) as listen:
        listen.join()