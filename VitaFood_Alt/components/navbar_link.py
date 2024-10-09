import reflex as rx 


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color="#203534"), href=url
    )
