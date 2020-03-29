import typer

from colab_cli.gdrive_auth import drive_auth
from colab_cli.utilities.checks import check_client_secret_exists
from colab_cli.utilities.files import create_new_file, get_file_meta
from colab_cli.utilities.folders import get_colab_folder_id, fold_struct_gen, delete_folder


def cli_update(folder_struct_list, upload_file_name, upload_file_abs_path):
    """
    Replace (Remote)ipynb in google colab with local ipynb
    :param folder_struct_list:
    :param upload_file_name:
    :param upload_file_abs_path:
    """
    check_client_secret_exists()
    total = 100
    with typer.progressbar(length=total) as progress:
        drive = drive_auth()
        progress.update(15)

        COLAB_NB_FOLD_ID = get_colab_folder_id(drive)
        progress.update(30)

        final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
        progress.update(45)

        delete_folder(drive, upload_file_name, final_folder_id)
        progress.update(60)

        new_file_metadata = get_file_meta(upload_file_name, final_folder_id)
        new_file_id = create_new_file(drive, new_file_metadata, upload_file_abs_path, upload_file_name, final_folder_id)
        # print(f"new colab file id is {new_file_id}")
        progress.update(100)

        message = f"\n {upload_file_name} in google drive updated with the local file"
        message = typer.style(message, fg=typer.colors.GREEN, bold=True)
        typer.echo(message)