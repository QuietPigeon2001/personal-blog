"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    # The hyperlinks for my social handles.
    resume_url: str = "https://drive.google.com/file/d/17lpKm8VZeLgjNqbrI3WYEWQ5ZF9vaL2y/view?usp=sharing"
    email_url: str = "mailto:homoreen@gmail.com"
    linkedin_url: str = "https://www.linkedin.com/in/moreen-h-93b251214/"
    github_url: str = "https://github.com/QuietPigeon2001"


def social_handles():
    return rx.hstack(
        rx.link(
            "Email",
            href=State.email_url,
        ),
        rx.link(
            "Resume",
            href=State.resume_url,
        ),
        rx.link(
            "Linkedin",
            href=State.linkedin_url,
        ),
        rx.link(
            "Github",
            href=State.github_url,
        ),
        spacing="2em"
    )


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.center(
            rx.vstack(
                rx.heading("Hi, I am Moreen."),
                rx.text("📍 Kyoto, Japan"),
                rx.divider(),
                social_handles(),
                spacing="2em",
                padding="10%",
            ),
        )
    )


# Add state and page to the app.
style = {
    "font_family": "SanFranciscoText, sans-serif",
}
app = rx.App(state=State, style=style)
app.add_page(index)
app.compile()
