from time import sleep
from gpiozero import CamJamKitRobot
from pynput.keyboard import Listener
from pynput.keyboard import Key
from pynput import keyboard

robot = CamJamKitRobot() 

leftMotorSpeed = 1
rightMotorSpeed = 1


motorFWD = (leftMotorSpeed, rightMotorSpeed)
motorBCK = (-leftMotorSpeed, -rightMotorSpeed)
motorLFT = (-leftMotorSpeed, rightMotorSpeed)
motorRGT = (leftMotorSpeed, -rightMotorSpeed)
	
def on_press(key):
	if key == Key.up: 
		robot.value = motorFWD
		print(" We move ahead " + str(key))
	elif key == Key.down:
		robot.value = motorBCK
		print(" We move backwards")
	elif key == Key.left:
		robot.value = motorLFT
		print(" We move left")
	elif key == Key.right:
		robot.value = motorRGT
		print(" We move Right")
		

		
	
def on_release(Key):
	robot.stop()
	print("stop moving")
	
with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()	

		
		
		
#robot.value = motorFWD


#listener = Keyboard.Listener(on_press=on_press)
#listener.start()
#listener.join()













