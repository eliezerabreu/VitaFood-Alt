import reflex as rx 
from VitaFood_Alt.styles.colors import Color, Textcolor
import VitaFood_Alt.styles.styles as styles


def card_nutritions() -> rx.Component:
    return rx.box(
        rx.center(
            rx.flex(
                rx.box(
                    background= "center/cover url('/Nutritionist_card.webp')",
                    width="40%",
                    height="400px",
                    margin=styles.size.BIG.value,
                    border_radius=styles.size.DEFAULT.value,
                    box_shadow="3px 3px 5px rgba(0, 0, 0, 0.4)"
                    ),
                rx.box(
                    rx.vstack(
                        rx.heading("Nourish Your Body, Elevate Your Life",  as_="h3", color=Color.PRIMARY.value, width="auto"),
                        rx.text(
                            "At VitaFood, we are dedicated to helping you achieve optimal health through a comprehensive approach. With personalized guidance from our nutritionists, you’ll receive a health plan tailored to your specific needs, complemented by high-quality supplements from the Tropical Oasis brand. Additionally, our Pranzo restaurant offers delicious and nutritious options that align with your meal plan. This unique combination creates the perfect synergy for caring for your health in a complete and effective way.",
                            color=Textcolor.BODY.value,
                            max_width="420px",
                            padding_top=styles.size.DEFAULT.value
                            ),
                        width="100%",
                        height="400px",
                        border_style="solid",
                        border_width="2px",
                        border_radius=styles.size.DEFAULT.value,
                        margin=styles.size.BIG.value,
                        padding=styles.size.BIG.value,
                        align="center",
                        box_shadow="3px 3px 5px rgba(0, 0, 0, 0.4)"

                    )
                    ),
                width="80%",
                height="100%", spacing="3",
                justify="center",
            ),
        ),
        width="100%",
        min_height="400px",
        background=Color.BACKGROUND.value
    )