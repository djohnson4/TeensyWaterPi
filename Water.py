import threading
import time
import atexit
import serial

pump = 3
floor = 20

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pump, GPIO.OUT)

class Hacer(object):
	prender = "on"
	apagar = "off"

def threaded(job_func, action=Hacer.prender, tiempo=None):
    job_thread = threading.Thread(target=job_func, kwargs={'action': action, 'tiempo': tiempo})
    job_thread.start()

def water():
	toggleComponent(pump, Hacer.prender, tiempo = 3)
	log()
	
def log(value):
    try:
		with open("moist.csv", "a") as f:
		    writer = csv.writer(f, delimiter = ",")
			writer.writerow([time.time(), value)
    except:
        print("KeyboardInterrupt")
		break
	f = open("last_watered.txt", "a")
    f.write(value)
    f.close()

def toggleComponent(pin, action=Hacer.prender, tiempo=None):
	if (tiempo is not None):
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(tiempo)
		GPIO.output(pin, GPIO.LOW)
	else:
		if action == Hacer.prender: GPIO.output(pin, GPIO.HIGH)
		else: GPIO.output(pin, GPIO.LOW)

def exit_handler():
    GPIO.cleanup()

atexit.register(exit_handler)


s = serial.Serial('/dev/ttyUSB0', 9600)
s.flushInput()
while 1:
    if(s.in_waiting > 0):
	    line = s.readline()
		if line <= floor:
		    water()

while True:
    schedule.run_pending()
    time.sleep(1)