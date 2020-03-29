import typer
from pathlib import Path


def check_client_secret_exists():
    APP_NAME = "colab-cli"
    app_dir = typer.get_app_dir(APP_NAME)
    client_secrets_path = Path(app_dir) / 'client_secrets.json'
    if not client_secrets_path.is_file():
        typer.echo("client_secrets.json file is not set yet, set using colab-cli set-config client_secrets.json")
        raise typer.Exit()