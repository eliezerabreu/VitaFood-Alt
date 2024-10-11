import reflex as rx 
from VitaFood_Alt.styles.colors import Color
from enum import Enum

class size(Enum):
    
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"
    BIGGER = "3em"

MAX_WIDTH = "35em"

BASE_STYLE = {
    
    "background_color": Color.BACKGROUND.value 
}