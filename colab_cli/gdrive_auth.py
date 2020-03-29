from pathlib import Path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import typer

APP_NAME = "colab-cli"
app_dir = typer.get_app_dir(APP_NAME)
client_secrets_path = Path(app_dir) / 'client_secrets.json'
mycreds_path = Path(app_dir) / 'mycreds.txt'

GoogleAuth.DEFAULT_SETTINGS[
    'client_config_file'] = client_secrets_path


def drive_auth():
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile(mycreds_path)
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile(mycreds_path)

    drive = GoogleDrive(gauth)

    return drive
