import reflex as rx 
from VitaFood_Alt.components.navbar_link import navbar_link


def header() -> rx.Component:
    return rx.center(
        
        rx.flex(
                rx.center(
                    
                    rx.image(src="/logovitafood.png", width="100px", height="auto"),
                    width="20%",
                    height="100%"),
                rx.box(
                    rx.hstack(
                        navbar_link("Home", "/#", "#203534"),
                        navbar_link("About", "/#", "#203534"),
                        navbar_link("Contact", "/#", "#203534"),
                        navbar_link("FAQ", "/#", "#203534"),
                        navbar_link("Nutritions", "/#", "#203534"),
                        navbar_link("Pranzo", "/#", "#203534"),
                        navbar_link("Tropical Oasis", "/#", "#203534"),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button(
                                    rx.text(
                                        "Users",
                                        size="4",
                                        weight="medium",
                                        color="#203534"
                                    ),
                                    rx.icon("chevron-down", color="#203534"),
                                    weight="medium",
                                    variant="ghost",
                                    size="3",
                                ),
                            ),
                            rx.menu.content(
                                rx.menu.item("Login"),
                                rx.menu.item("Register")
                            ),
                            
                        ),
                        justify="end",
                        align="center",
                        width="100%",
                    height="100%",
                    spacing="5"
                    
                    ), 
                    width="100%",
                    height="100%"
            ),
            width="80%",
            height="100%"
        ),
        background="#F0D05A",
        width="100%",
        height="15vh"
    )
