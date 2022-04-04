import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Christmas Catch"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 40
FIELD_BOTTOM = 200
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "christmas_catch/assets/fonts/zorque.otf"
FONT_FILE_LOGO = "christmas_catch/assets/fonts/font_logo.otf"
FONT_SMALL = 32
FONT_LARGE = 48
FONT_SIZE_LOGO = 60

# SOUND
BOUNCE_SOUND = "christmas_catch/assets/sounds/boing.wav"
WELCOME_SOUND = "christmas_catch/assets/sounds/christmas.mp3"
OVER_SOUND = "christmas_catch/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
RESTART = "r"
MENU = "m"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# BACKGROUND
BACKGROUND_GROUP = "background"
BACKGROUND_IMAGE = "christmas_catch/assets/images/background.png"
MENU_IMAGE = "christmas_catch/assets/images/menu_background.png"

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# SANTA
SANTA_GROUP = "santas"
SANTA_IMAGE = "christmas_catch/assets/images/000.png"
SANTA_WIDTH = 135
SANTA_HEIGHT = 130
SANTA_VELOCITY = 3
MAX_X = 900
MAX_Y = 600

# BOY
BOY_GROUP = "boys"
BOY_IMAGE = "christmas_catch/assets/images/100.png"
BOY_WIDTH = 120
BOY_HEIGHT = 161
BOY_VELOCITY = 7

# GIFT/REGALOS
GIFT_GROUP = "gifts"
GIFT_QUANTITY = 30
GIFT_GREEN_IMAGES = "christmas_catch/assets/images/010.png"
GIFT_RED_IMAGES = "christmas_catch/assets/images/020.png"
GIFT_WIDTH = 50
GIFT_HEIGHT = 51
GIFT_GREEN_POINTS = 50
GIFT_RED_POINTS = 100

#COAL
COAL_IMAGE = "christmas_catch/assets/images/104.png"
COAL_POINTS = -50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"