import reflex as rx 
from VitaFood_Alt.styles.colors import Color
import VitaFood_Alt.styles.styles as styles
import VitaFood_Alt.components.constant as constant

def video_section() -> rx.Component:
    return rx.box(
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.text("Meet Tropical Oasis", 
                            size="8",
                            color=Color.THREE.value, 
                            margin_top=styles.size.BIG.value, 
                            weight="medium",
                            align="center"),
                        rx.video(
                            url=constant.TROPICAL_OASIS_VIDEO,
                            max_width=styles.MAX_WIDTH,
                            height="320px",
                            ),
                        
                        align="center", 
                        width="100%"
                    ),
                    text_align="center",
                    width="80%",
                    height="100%"
                ),
            ),
        background="linear-gradient(45deg, #658267, #203534)",
        
        width= "100%",
        height= "500px",
        padding_bottom=styles.size.DEFAULT.value,
        margin= ""
    )