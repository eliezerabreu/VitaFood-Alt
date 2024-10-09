import reflex as rx 
from VitaFood_Alt.styles.colors import Color, Textcolor

def footer() -> rx.Component:
    return rx.box(
        rx.center(
            rx.flex(
                rx.vstack(
                        rx.box(
                            rx.image(
                                src="/quality.webp",
                                width="100%",
                                height="auto",
                            ),
                            
                            ),
                        rx.hstack(
                                rx.image(
                                    src="/facebook_icon.svg",
                                    width="3em",
                                    height="auto",
                                ),
                                rx.image(
                                    src="/formkit_twitter.svg",
                                    width="3em",
                                    height="auto",
                                ),
                                rx.image(
                                    src="/whatsapp_icon.svg",
                                    width="3em",
                                    height="auto",
                                ),
                                rx.image(
                                    src="/telegram_icon.svg",
                                    width="3em",
                                    height="auto",
                                ),
                                padding_y="2%"
                            ),
                    align="center",
                    width="50%",
                    height="400px",
                    margin_y="2em",
                ),
                rx.box(
                    rx.vstack(
                        rx.link(
                            rx.text("Nutrition")
                        ),
                        rx.link(
                            rx.text("FAQ")
                        ),
                        rx.link(
                            rx.text("Pranzo")
                        ),
                        rx.link(
                            rx.text("Tropical Oasis")
                        ),
                        rx.link(
                            rx.text("About")
                        ),
                        rx.link(
                            rx.text("Contact")
                        ),
                        margin_x="7em",
                        margin_y="2em"
                    ),
                    width="50%"
                    ),
                width="80%",
                height="100%", spacing="3",
                justify="center",
            ),
            
            
        ),
        width="100%",
        min_height="400px",
        background=Color.PRIMARY.value
    )