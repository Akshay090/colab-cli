import json

import typer
from pathlib import Path

APP_NAME = "colab-cli"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
client_secrets_path = app_dir / 'client_secrets.json'
config_path = app_dir / 'config.json'


def check_client_secret_exists():
    if not client_secrets_path.is_file():
        typer.echo("client_secrets.json file is not set yet, set using colab-cli set-config client_secrets.json")
        raise typer.Exit()


def check_all_config():
    check_client_secret_exists()

    if not config_path.is_file():
        typer.echo("auth user not set, set it using colab-cli set-auth-user")
        raise typer.Exit()

    with open(config_path) as file:
        config_data = json.load(file)
        AUTH_USER_ID = config_data["auth_user_id"]

    if AUTH_USER_ID:
        return AUTH_USER_ID
    if not AUTH_USER_ID:
        typer.echo("auth user not set, set it using colab-cli set-auth-user")
        raise typer.Exit()
