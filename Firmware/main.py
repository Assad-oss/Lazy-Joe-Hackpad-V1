import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry

keyboard = KMKKeyboard()

# 1. Setup Media Keys (Volume/Brightness)
keyboard.extensions.append(MediaKeys())

# 2. Rotary Encoder Setup (Pins 1 & 2 from your schematic)
# Clockwise = TAB, Counter-Clockwise = Shift+TAB
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP26, board.GP27, None, False),)
encoder_handler.map = (((KC.TAB, KC.LSFT(KC.TAB)),),)

# 3. Pin Mapping for SW1-SW4
# SW1=GP29, SW2=GP6, SW3=GP7, SW4=GP0
keyboard.col_pins = (board.GP29, board.GP6, board.GP7, board.GP0)
keyboard.row_pins = (board.GP28,) # Dummy row for simple push buttons
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 4. Keymap for the Switches
keyboard.keymap = [
    [
        KC.VOLU, # SW1: Volume Up
        KC.VOLD, # SW2: Volume Down
        KC.BRID, # SW3: Brightness Up (Media Key)
        KC.BRIU, # SW4: Brightness Down (Media Key)
    ]
]

# 5. OLED Display Setup (128x32)
# Connect OLED SDA to GP4 and SCL to GP5
display = Display(
    displayer=TextEntry,
    width=128,
    height=32,
    i2c=board.I2C(),
    device_address=0x3C,
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
