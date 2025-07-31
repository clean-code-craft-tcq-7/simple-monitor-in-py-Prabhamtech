from time import sleep
import sys
 
def blink_alert(message, duration=6):
    print(message)
    for _ in range(duration):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(1)
 
def vitals_ok(temperature, pulseRate, spo2):
    if (temperature_ok(temperature) and pulse_rate_ok(pulseRate) and spo2_ok(spo2)):
        return True
    return False

def temperature_ok(temperature):
    if temperature > 102 or temperature < 95:
        blink_alert('Temperature critical!')
        return False
    return True

def pulse_rate_ok(pulseRate):
    if pulseRate < 60 or pulseRate > 100:
        blink_alert('Pulse Rate is out of range!')
        return False
    return True

def spo2_ok(spo2):
    if spo2 < 90:
        blink_alert('Oxygen Saturation out of range!')
        return False
    return True