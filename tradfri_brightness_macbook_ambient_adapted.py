# POC: Use Macbook brigthness level (modulated via ambient light sensor) as base for
# adapting IKEA tradfri brightness
#
# REQUIREMENTS
#
# installed
# hombrew:
# - brightness
# pip:
# - sh
# - pytradfri
#
# run python3 -i -m pytradfri IP_OF_GATEWAY


import sh
import time

brightness = sh.Command("brightness")


def read_macbook_brightness_level():
    result = brightness("-l")
    return float(''.join([c for c in str(result.stdout).split('brightness')[-1].strip() if c.isdigit() or c == '.']))


def set_ikea_lights_brightness(new_level):
    for light in lights:
        api(light.light_control.set_dimmer(new_level))


def calculate_desired_brightness_level(screen_brightness):
    return int(254*(1-macbook_brightness_level))

while True:
    macbook_brightness_level = read_macbook_brightness_level()
    print(macbook_brightness_level)
    new_level = calculate_desired_brightness_level(macbook_brightness_level)
    set_ikea_lights_brightness(new_level)
    time.sleep(10)
