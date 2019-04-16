from pirc522 import RFID
import signal
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

print "HC-SR04 mesafe sensoru"
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True
GPIO.output(7, False)
while True:
	rdr.wait_for_tag()
	(error, data) = rdr.request()
	if not error:
		print("\nKart Algilandi!")
		(error, uid) = rdr.anticoll()
		if not error:
			# Print UID
			kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
			print(kart_uid)
			if kart_uid == "236 211 59 7 3":
				print("LED Yandi!")
				GPIO.output(7, True)
				while True:
                                    GPIO.output(13, False)
                                    print "Olculuyor..."
                                    time.sleep(0.2)
				    GPIO.output(13, True)
				    time.sleep(0.00001)
				    GPIO.output(13, False)
		                    while GPIO.input(15)==0:
				    	pulse_start = time.time()
				while GPIO.input(15)==1:
					pulse_end = time.time()
				pulse_duration = pulse_end - pulse_start
				distance = pulse_duration * 17150
				distance = round(distance, 2)
				if distance > 2 and distance < 30:
					GPIO.output(11,GPIO.HIGH)
				else
					GPIO.output(11,GPIO.LOW)
