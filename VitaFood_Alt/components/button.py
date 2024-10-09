import reflex as rx 
from VitaFood_Alt.styles.colors import Color

def button(text: str) -> rx.Component: 
    return rx.button(
        text, 
        background="linear-gradient(45deg, #203534, #658267)", 
        _hover={"background": "linear-gradient(45deg, #658267, #203534)"},
        padding_x="2em",
        padding_y="1em",
        border_radius="16px"      
    )