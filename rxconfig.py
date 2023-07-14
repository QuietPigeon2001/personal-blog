import reflex as rx

class PersonalblogConfig(rx.Config):
    pass

config = PersonalblogConfig(
    app_name="personal_blog",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)