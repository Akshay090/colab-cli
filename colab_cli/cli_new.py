import typer
import webbrowser
from colab_cli.gdrive_auth import drive_auth
from colab_cli.utilities.checks import check_all_config
from colab_cli.utilities.files import create_new_file, get_file_meta
from colab_cli.utilities.folders import fold_struct_gen, get_colab_folder_id


def cli_new(folder_struct_list, upload_file_name, upload_file_abs_path):

    AUTH_USER_ID = check_all_config()

    total = 100
    with typer.progressbar(length=total) as progress:
        drive = drive_auth()
        progress.update(15)
        COLAB_NB_FOLD_ID = get_colab_folder_id(drive)
        progress.update(30)
        final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
        progress.update(45)
        new_file_metadata = get_file_meta(upload_file_name, final_folder_id)
        progress.update(60)
        new_file_id = create_new_file(drive, new_file_metadata,
                                      upload_file_abs_path, upload_file_name,
                                      final_folder_id)
        progress.update(75)
        colab_url = f'https://colab.research.google.com/drive/{new_file_id}?authuser={AUTH_USER_ID}'
        drive_folder_url = f'https://drive.google.com/drive/u/{AUTH_USER_ID}/folders/{final_folder_id}'
        progress.update(90)
        webbrowser.open(url=colab_url)
        progress.update(100)

        # message = f"\n {upload_file_name} created in drive folder"
        # message = typer.style(message, fg=typer.colors.GREEN, bold=True)
        # typer.echo(message)
        message = f"\n drive folder url: {drive_folder_url}"
        message = typer.style(message, fg=typer.colors.CYAN, bold=True)
        typer.echo(message)

        message = f"\n colab file url: {colab_url}"
        message = typer.style(message, fg=typer.colors.BRIGHT_CYAN, bold=True)
        typer.echo(message)
