from pathlib import Path
import typer
import webbrowser
import json
from colab_cli.gdrive_auth import drive_auth
from colab_cli.utilities.checks import check_client_secret_exists
from colab_cli.utilities.files import create_new_file, get_file_meta
from colab_cli.utilities.folders import fold_struct_gen, get_colab_folder_id

APP_NAME = "colab-cli"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
client_secrets_path = app_dir / 'client_secrets.json'
config_path = app_dir / 'config.json'


def cli_open(folder_struct_list, upload_file_name, upload_file_abs_path):
    check_client_secret_exists()

    if not config_path.is_file():
        typer.echo("auth user not set, set it using colab-cli set-auth-user")
        raise typer.Exit()

    with open(config_path) as file:
        config_data = json.load(file)
        AUTH_USER_ID = config_data["auth_user_id"]

    if not AUTH_USER_ID:
        typer.echo("auth user not set, set it using colab-cli set-auth-user")
        raise typer.Exit()

    drive = drive_auth()

    COLAB_NB_FOLD_ID = get_colab_folder_id(drive)

    # print(COLAB_NB_FOLD_ID)

    final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
    # print(f"final folder id {final_folder_id}")
    new_file_metadata = get_file_meta(upload_file_name, final_folder_id)
    new_file_id = create_new_file(drive, new_file_metadata, upload_file_abs_path, upload_file_name, final_folder_id)
    # print(f"new colab file id is {new_file_id}")

    colab_url = f'https://colab.research.google.com/drive/{new_file_id}?authuser={AUTH_USER_ID}'
    webbrowser.open(url=colab_url)
