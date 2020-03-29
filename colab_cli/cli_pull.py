from pathlib import Path
import typer

from colab_cli.gdrive_auth import drive_auth
from colab_cli.utilities.checks import check_client_secret_exists
from colab_cli.utilities.files import download_file
from colab_cli.utilities.folders import fold_struct_gen, get_colab_folder_id


def cli_pull(folder_struct_list, upload_file_name, upload_file_abs_path):
    check_client_secret_exists()
    drive = drive_auth()

    COLAB_NB_FOLD_ID = get_colab_folder_id(drive)

    print(COLAB_NB_FOLD_ID)

    final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
    # print(f"final folder id {final_folder_id}")

    download_file(drive, upload_file_name, upload_file_abs_path, final_folder_id)
