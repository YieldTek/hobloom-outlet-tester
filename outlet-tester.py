import time
import Adafruit_BBIO.GPIO as GPIO

GPIO_PINS = [
    'P9_12',
    'P9_23',
    'P9_25',
    'P9_27',
    'P9_30',
    'P9_41',
    'P8_7',
    'P8_8',
    'P8_9',
    'P8_10',
    'P8_11',
    'P8_12',
    'P8_14',
    'P8_15',
    'P8_16',
    'P8_17',
    'P8_18',
    'P8_26'
]

pins_used = []

def setupPins():
    print 'Turning off all outlets before starting test'
    for pin in pins_used:
        GPIO.setup(pin, GPIO.OUT)
        time.sleep(2)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(2)

def testOutlets():
    for pin in pins_used:
        print "Powering on outlet at pin: {0}".format(pin)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(10)
        print "Powering off outlet at pin: {0}".format(pin)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(2)

def collectPins():
    print 'Please enter the pin your first outlet is connected to(Example: "P8_9" or "P9_12"):'
    while True:
        pin = raw_input()
        if str(pin).upper() in GPIO_PINS:
            pins_used.append(str(pin).upper())
            print 'Would you like to enter a pin for another outlet[Y/n]?'
            more_pins = raw_input()
            if ('Y' in str(more_pins).upper()):
                print 'Please enter pin connecting outlet to BeagleBone:'
                continue
            return
        print 'You have enterd an invalid pin, please try again.  An example entry is "P8_9" or "P9_12"'

def main():
    collectPins()
    setupPins()
    testOutlets()

if __name__ == '__main__':
    main()