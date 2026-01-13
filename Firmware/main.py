import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled import PegOLED

keyboard = KMKKeyboard()

# 1. Add Extensions
keyboard.extensions.append(MediaKeys())

# 2. Setup OLED (GPIO7=SCL, GPIO6=SDA)
i2c_bus = busio.I2C(board.GP7, board.GP6)
oled_ext = PegOLED(i2c_device=i2c_bus, display_width=128, display_height=32)
keyboard.extensions.append(oled_ext)

# 3. Define Pins (Matches your image_f325f5.png)
# SW1=GP3, SW2=GP4, SW3=GP2, SW4=GP1
PINS = [board.GP3, board.GP4, board.GP2, board.GP1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# 4. Custom OLED Scene for "3 Second" Rule
class FeedbackScene:
    def __init__(self):
        self.name = "Feedback"
        self.last_key = ""
        self.timer = 0

    def update(self, oled):
        if self.timer > 0:
            oled.fill(0)
            oled.text(f"Switch: {self.last_key}", 20, 10, 1)
            oled.show()
            self.timer -= 1
        else:
            oled.fill(0) # Clear after 3 seconds
            oled.show()

feedback = FeedbackScene()
oled_ext.scenes = [feedback]

# KC.VOLU/VOLD = Volume, KC.BRID/BRIU = Brightness
keyboard.keymap = [
    [
        KC.VOLU, # SW1
        KC.VOLD, # SW2
        KC.BRIU, # SW3
        KC.BRID  # SW4
    ]
]

# updates the oled whenever a key is pressed
def after_matrix_scan(keyboard):
    if keyboard.matrix.update():
        if keyboard.matrix.event.pressed:
            # Show switch number (1-4)
            feedback.last_key = str(keyboard.matrix.event.key_number + 1)
            feedback.timer = 300 # Roughly 3 seconds depending on scan rate

keyboard.after_matrix_scan = after_matrix_scan

if __name__ == '__main__':

    keyboard.go()
