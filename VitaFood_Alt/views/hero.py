import reflex as rx 
from VitaFood_Alt.components.button import button
from VitaFood_Alt.styles.colors import Color, Textcolor

def hero() -> rx.Component:
    return rx.box(
            rx.center(
                rx.vstack(
                    rx.heading("Nourish Your Body, Elevate Your Life", size="8"),
                    rx.text("Discover the power of healthy eating and liquid supplements for optimal wellness and vitality."),
                    button("Information")
                ),
                height= "100%"
            ),
    background= "center/cover url('/heroHome.png')",
    width= "100%",
        height= "450px",
        margin= "0"
    )