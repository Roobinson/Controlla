from gpiozero import Button
 
leftButton = Button(2)
downButton = Button(3)
upButton = Button(4)
rightButton = Button(5)
okButton = Button(6)
 
while True:
    leftButton.wait_for_press()
    print("Left")
    downButton.wait_for_press()
    print("Down")
    upButton.wait_for_press()
    print("Up")
    rightButton.wait_for_press()
    print("Right")
    okButton.wait_for_press()
    print("Select")
