# boot.py for Adafruit NeoKey Trinkey
# The drive will not be activated unless you press a key.
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode  # pylint: disable=unused-import
from digitalio import DigitalInOut, Pull
import storage

print("hello from boot.py")  # see this in 'boot_out.txt'

# create the switch, add a pullup, start it with not being pressed
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

if not button.value:
    storage.disable_usb_drive()    # Turn off CIRCUITPY.
