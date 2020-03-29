def get_colab_folder_id(drive):
    # get Colab Notebooks id, creates if not exist and return it
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    COLAB_NB_FOLD_ID = None

    for file in file_list:
        if file['title'] == "Colab Notebooks":
            COLAB_NB_FOLD_ID = file['id']
    if COLAB_NB_FOLD_ID:
        return COLAB_NB_FOLD_ID
    else:
        folder_meta = get_folder_meta("Colab Notebooks", "root")
        colab_folder_id = create_new_folder(drive, folder_meta)
        return colab_folder_id


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
    # print('New folder created: ' + folder_new['title'] + " " + folder_new['id'])
    upload_folder_id = folder_new['id']  # Get the folder id
    return upload_folder_id


def fold_struct_gen(drive, folder_parent_id, folder_struct_list):
    PARENT_ID = folder_parent_id
    for current_folder_name in folder_struct_list:
        # print(f"PARENT_ID is {PARENT_ID}")
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


def delete_folder(drive, file_name, parent_id):
    fileList = drive.ListFile({'q': f"'{parent_id}' in parents and trashed=false"}).GetList()
    # CURRENT_FILE_EXIST = False
    for file in fileList:
        # print('Title: %s, ID: %s' % (file['title'], file['id']))
        if file['title'] == file_name:  # folder already exists
            CURRENT_FILE_EXIST = True
            file.Trash()
