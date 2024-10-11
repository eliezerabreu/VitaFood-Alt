import reflex as rx 
import VitaFood_Alt.styles.styles as styles

def button(text: str) -> rx.Component: 
    return rx.button(
        text, 
        background="linear-gradient(45deg, #203534, #658267)", 
        _hover={"background": "linear-gradient(45deg, #658267, #203534)"},
        padding_x=styles.size.BIG.value,
        padding_y=styles.size.DEFAULT.value,
        border_radius=styles.size.DEFAULT.value     
    )