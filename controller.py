from gpiozero import Button
 
leftButton = Button(2)
downButton = Button(3)
upButton = Button(4)
rightButton = Button(5)
okButton = Button(6)
 
def left():
    print("Left")
def down():
    print("Down")
def up():
    print("Up")
def right():
    print("Right")
def select():
    print("Start/Select")
     
leftButton.when_pressed = left
downButton.when_pressed = down
upButton.when_pressed = up
rightButton.when_pressed = right
okButton.when_pressed = select
