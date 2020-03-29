from pathlib import Path
import typer
from send2trash import send2trash

from colab_cli.gdrive_auth import drive_auth

APP_NAME = "colab-cli"
app_dir = typer.get_app_dir(APP_NAME)
client_secrets_path = Path(app_dir) / 'client_secrets.json'


def cli_pull(folder_struct_list, upload_file_name, upload_file_abs_path):
    print("download fxn")
    if not client_secrets_path.is_file():
        typer.echo("client_secrets.json file is not set yet, set using colab-cli set-config client_secrets.json")
        raise typer.Exit()
    drive = drive_auth()
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    COLAB_NB_FOLD_ID = None

    for file in file_list:
        print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == "Colab Notebooks":
            COLAB_NB_FOLD_ID = file['id']

    # print(COLAB_NB_FOLD_ID)

    final_folder_id = fold_struct_gen(drive, COLAB_NB_FOLD_ID, folder_struct_list)
    print(f"final folder id {final_folder_id}")
    # new_file_metadata = get_file_meta(upload_file_name, final_folder_id)
    # new_file_id = create_new_file(drive, new_file_metadata, upload_file_abs_path, upload_file_name, final_folder_id)
    download_file(drive, upload_file_name, upload_file_abs_path, final_folder_id)


def get_folder_meta(folder_name, parent_id):
    folder_metadata = {
        'title': f"{folder_name}",
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{'id': parent_id}]
    }
    return folder_metadata


def create_new_folder(drive, folder_metadata):
    folder_new = drive.CreateFile(folder_metadata)
    folder_new.Upload()
    print('New folder created: ' + folder_new['title'] + " " + folder_new['id'])
    upload_folder_id = folder_new['id']  # Get the folder id
    return upload_folder_id


def fold_struct_gen(drive, folder_parent_id, folder_struct_list):
    PARENT_ID = folder_parent_id
    for current_folder_name in folder_struct_list:
        print(f"PARENT_ID is {PARENT_ID}")
        fileList = drive.ListFile({'q': f"'{PARENT_ID}' in parents and trashed=false"}).GetList()
        CURRENT_FOLDER_EXIST = False
        for file in fileList:
            # print('Title: %s, ID: %s' % (file['title'], file['id']))
            if file['title'] == current_folder_name:  # folder already exists
                CURRENT_FOLDER_EXIST = True
                PARENT_ID = file['id']

        if CURRENT_FOLDER_EXIST is False:
            # create new folder
            new_folder_meta = get_folder_meta(current_folder_name, PARENT_ID)
            new_folder_id = create_new_folder(drive, new_folder_meta)
            PARENT_ID = new_folder_id
    return PARENT_ID


def get_file_meta(file_name, parent_id):
    file_metadata = {
        'title': f"{file_name}",
        'mimeType': 'application/vnd.google.colaboratory',
        "parents": [{"kind": "drive#fileLink",
                     "id": parent_id}]
    }
    return file_metadata


def create_new_file(drive, file_metadata, file_path, file_name, parent_id):
    fileList = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    CURRENT_FOLDER_EXIST = False
    for file in fileList:
        # print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == file_name:  # folder already exists
            CURRENT_FOLDER_EXIST = True

    if CURRENT_FOLDER_EXIST:
        print(f"file already exist")
        return None
    file_new = drive.CreateFile(file_metadata)
    file_new.SetContentFile(str(file_path))  # Set the content to the taken image
    file_new.Upload()  # Upload it
    print('New file created:    ' + file_new['title'] + " " + file_new['id'])
    new_file_id = file_new['id']  # Get the folder id
    return new_file_id


def download_file(drive, file_name,file_abs_path,  parent_id):
    fileList = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    CURRENT_FILE_EXIST = False
    for file in fileList:
        # print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == file_name:  # folder already exists
            CURRENT_FILE_EXIST = True
            print(file_abs_path)
            send2trash(str(file_abs_path))
            print("local file to trash")
            file.GetContentFile(file['title'])

    if not CURRENT_FILE_EXIST:
        print(f"file don't exist")
