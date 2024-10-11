import reflex as rx 
from VitaFood_Alt.styles.colors import Color


def navbar_link(text: str, url: str, color: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color=color), href=url, 
        is_external=True,
        text_decoration= "none",
        _hover=(
            rx.text(size="6")
        )
    )
