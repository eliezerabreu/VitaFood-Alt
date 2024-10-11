import reflex as rx 
from VitaFood_Alt.styles.colors import Color, Textcolor
from VitaFood_Alt.components.navbar_link import navbar_link
import VitaFood_Alt.styles.styles as styles


def footer() -> rx.Component:
    return rx.center(
                rx.center(
                    rx.vstack(
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
                                                width=styles.size.BIGGER.value,
                                                height="auto",
                                            ),
                                            rx.image(
                                                src="/formkit_twitter.svg",
                                                width=styles.size.BIGGER.value,
                                                height="auto",
                                            ),
                                            rx.image(
                                                src="/whatsapp_icon.svg",
                                                width=styles.size.BIGGER.value,
                                                height="auto",
                                            ),
                                            rx.image(
                                                src="/telegram_icon.svg",
                                                width=styles.size.BIGGER.value,
                                                height="auto",
                                            ),
                                            padding_y="2%"
                                        ),
                                align="center",
                                width="50%",
                                height="250px",
                                margin_y=styles.size.BIG.value,
                            ),
                            rx.box(
                                rx.vstack(
                                    navbar_link("Home", "/#", "#658267"),
                                    navbar_link("About", "/#", "#658267"),
                                    navbar_link("Contact", "/#", "#658267"),
                                    navbar_link("FAQ", "/#", "#658267"),
                                    navbar_link("Nutritions", "/#", "#658267"),
                                    navbar_link("Pranzo", "/#", "#658267"),
                                    navbar_link("Tropical Oasis", "/#", "#658267"),
                                    margin_x="7em",
                                    margin_y="2em"
                                    ),
                                width="50%",
                                align="center",
                                ),
                            width="100%",
                            align="center",
                        ),
                        rx.box(
                            rx.divider(size="4"),
                            rx.text("Contact",
                                    margin_top=styles.size.DEFAULT.value,
                                    size="5",
                                    ),
                            rx.text("Vitafood",
                                    margin_top=styles.size.DEFAULT.value,
                                    size="4",
                                    ),
                            rx.hstack(
                                rx.icon("phone"),
                                rx.text("Phone (+1) (682) 560 – 55780",
                                    margin_top="0em",
                                    size="4",
                                    ),
                                justify="center"
                            ),
                            rx.hstack(
                                rx.icon("mail"),
                                navbar_link("globalvitafoodenterprises@gmail.com","/#","#fffff"),
                                justify="center"
                            ),
                            rx.hstack(
                                rx.icon("locate-fixed",
                                    margin_top=styles.size.DEFAULT.value,
                                    ),
                                rx.text("3200 Alma dr suite c, Plano, Tx 75075",
                                    margin_top=styles.size.DEFAULT.value,
                                    size="4",
                                    ),
                                justify="center"
                            ),
                            rx.text("Accepted Payments",
                                    margin_top=styles.size.DEFAULT.value,
                                    size="4",
                                    ),
                            rx.text("Copyright © 2024 VitaFood | Powered by VitaFood",
                                    size="4",
                                    ),
                            
                            
                            text_align="center",
                            width="100%",
                            height="250px",
                            margin_y=styles.size.BIG.value
                        ),
                    width="100%",
                    ),
                    width="80%",
                ),
                
        width="100%",
        background="#203534"
    )