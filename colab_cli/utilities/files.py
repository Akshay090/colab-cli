from send2trash import send2trash


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
    NEW_FILE_ID = None
    for file in fileList:
        # print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == file_name:  # folder already exists
            CURRENT_FOLDER_EXIST = True
            NEW_FILE_ID = file['id']
    if CURRENT_FOLDER_EXIST:
        # print(f"file already exist")
        return NEW_FILE_ID
    file_new = drive.CreateFile(file_metadata)
    file_new.SetContentFile(str(file_path))  # Set the content to the taken image
    file_new.Upload()  # Upload it
    # print('New file created:    ' + file_new['title'] + " " + file_new['id'])
    new_file_id = file_new['id']  # Get the folder id
    return new_file_id


def download_file(drive, file_name, file_abs_path, parent_id):
    """
    download file from gdrive and move local file in file_abs_path to trash
    :param drive:
    :param file_name:
    :param file_abs_path:
    :param parent_id:
    :return:
    """
    fileList = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    CURRENT_FILE_EXIST = False
    for file in fileList:
        # print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == file_name:  # folder already exists
            CURRENT_FILE_EXIST = True
            # print(file_abs_path)
            send2trash(str(file_abs_path))
            # print("local file to trash")
            file.GetContentFile(file['title'])

    if not CURRENT_FILE_EXIST:
        pass
        # print(f"file don't exist")

