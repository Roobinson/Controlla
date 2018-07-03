from gpiozero import Button
from pyautogui import press, typewrite, hotkey
 
leftButton = Button(2)
downButton = Button(3)
upButton = Button(4)
rightButton = Button(5)
okButton = Button(6)
 
def buttonFun(direction):
    if direction == "left": press('a')
    elif direction == "down": press('s')
    elif direction == "up": press('w')
    elif direction == "right": press('d')
    elif direction == "select": press('space')
     
leftButton.when_pressed = buttonFun("left")
downButton.when_pressed = buttonFun("down")
upButton.when_pressed = buttonFun("up")
rightButton.when_pressed = buttonFun("right")
okButton.when_pressed = buttonFun("select")
