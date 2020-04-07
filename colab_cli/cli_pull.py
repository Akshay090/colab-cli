import typer
from colab_cli.gdrive_auth import drive_auth
from colab_cli.utilities.checks import check_all_config
from colab_cli.utilities.files import download_file
from colab_cli.utilities.folders import fold_struct_gen, get_colab_folder_id


def cli_pull(folder_struct_list, upload_file_name, upload_file_abs_path):
    """
    Replace local ipynb with (Remote)ipynb in google colab
    :param folder_struct_list:
    :param upload_file_name:
    :param upload_file_abs_path:
    """
    AUTH_USER_ID = check_all_config()

    total = 100
    with typer.progressbar(length=total) as progress:
        drive = drive_auth()
        progress.update(15)

        COLAB_NB_FOLD_ID = get_colab_folder_id(drive)
        progress.update(30)

        final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
        progress.update(45)

        download_file(drive, upload_file_name, upload_file_abs_path, final_folder_id)
        progress.update(100)

        message = f"\n local {upload_file_name} updated with the one in  google drive"
        message = typer.style(message, fg=typer.colors.GREEN, bold=True)
        typer.echo(message)
