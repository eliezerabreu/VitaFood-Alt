import reflex as rx 
from VitaFood_Alt.views.header import header
from VitaFood_Alt.views.hero import hero
from VitaFood_Alt.views.Card_Nutritions import card_nutritions
from VitaFood_Alt.views.video_section import video_section
from VitaFood_Alt.views.footer import footer
import VitaFood_Alt.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack( 
        header(),
        hero(),
        card_nutritions(),
        video_section(),
        footer(),
        gap="0"
    )

app = rx.App(
    styles=styles.BASE_STYLE
)
app.add_page(index)
app._compile()