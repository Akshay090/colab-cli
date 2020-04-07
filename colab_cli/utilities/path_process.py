from pathlib import Path
import git
import os

import typer
from git import InvalidGitRepositoryError

from colab_cli.utilities.git_root import Repo


def get_git_root(path):

    try:
        git_repo = Repo(path, search_parent_directories=True)
        return git_repo.working_tree_dir
    except InvalidGitRepositoryError as no_repo_error:
        message = f"no git repo initialized : please make sure you have initialized a git repo \n"
        message = typer.style(message, fg=typer.colors.BRIGHT_RED, bold=True)
        typer.echo(message)
        raise typer.Exit()


def process_file_path(file_path):
    git_root_path = get_git_root(file_path)

    base_folder_name = os.path.basename(git_root_path)
    rel_path = os.path.relpath(str(file_path), git_root_path)

    file_rel_path = os.path.join(base_folder_name, rel_path)
    folder_rel_path = os.path.dirname(file_rel_path)
    path_array_obj = Path(folder_rel_path)
    folder_struct_list = path_array_obj.parts
    upload_file_name = os.path.basename(str(file_path))
    # print(upload_file_name)
    # print(folder_struct_list)
    return folder_struct_list, upload_file_name, file_path
