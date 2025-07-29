from time import sleep
import sys
 
def blink_alert(message, duration=6):
    print(message)
    for _ in range(duration):
        for symbol in ['* ', ' *']:
            print(f'\r{symbol}', end='')
            sys.stdout.flush()
            sleep(1)
 
def vitals_ok(temperature, pulse_rate, spo2):
    if temperature > 102 or temperature < 95:
        blink_alert('Temperature critical!')
        return False
    if pulse_rate < 60 or pulse_rate > 100:
        blink_alert('Pulse Rate is out of range!')
        return False
    if spo2 < 90:
        blink_alert('Oxygen Saturation out of range!')
        return False
    return True