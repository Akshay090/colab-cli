from colab_cli.cli_pull import cli_pull
from colab_cli.cli_open import cli_open
from shutil import copy
from pathlib import Path
import typer
import git
import os
import time
import json


from colab_cli.cli_update import cli_update

APP_NAME = "colab-cli"
app_dir = typer.get_app_dir(APP_NAME)
app_dir = Path(app_dir)
config_path = app_dir / 'config.json'

app = typer.Typer()


def get_git_root(path):
    git_repo = git.Repo(path, search_parent_directories=True)
    return git_repo.working_tree_dir


@app.callback()
def callback():
    """
    Awesome colab cli
    """


@app.command()
def set_auth_user(user_no: str):
    """
      Set auth user
      """
    config = {'auth_user_id': user_no}
    print(config)
    print(config_path)
    with open(config_path, "w") as f:
        json.dump(config, f)


@app.command()
def print_user():
    """
      Set auth user
      """



@app.command()
def set_config(file_path: Path = typer.Argument(
    ...,
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)):
    """
      Set client_secrets.json for colab-cli
      """
    if file_path is None:
        typer.echo("No file")
        raise typer.Abort()
    if file_path.is_file():
        app_dir.mkdir(parents=True, exist_ok=True)
        copy(file_path, app_dir)
        typer.echo("Config File set Successfully")
    elif file_path.is_dir():
        typer.echo("is a directory")
    elif not file_path.exists():
        typer.echo("The file doesn't exist")


@app.command()
def open_nb(file_path: Path = typer.Argument(
    ...,
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)):
    """
    Open ipynb from colab,if not exist adds local file and open
    """
    start_time = time.time()
    if file_path is None:
        typer.echo("No file")
        raise typer.Abort()
    if file_path.is_file():
        start_time = time.time()
        git_root_path = get_git_root(file_path)

        base_folder_name = os.path.basename(git_root_path)
        rel_path = os.path.relpath(file_path, git_root_path)

        file_rel_path = os.path.join(base_folder_name, rel_path)
        folder_rel_path = os.path.dirname(file_rel_path)
        path_array_obj = Path(folder_rel_path)
        folder_struct_list = path_array_obj.parts
        upload_file_name = os.path.basename(file_path)
        print(upload_file_name)
        print(folder_struct_list)

        start_time = time.time()
        # print(f"relpath is {rel_path}")
        # folder_struct_list = rel_path.split(os.sep)  # list of file structure from base_folder to (including) file to open
        # print(f"{folder_struct_list}")
        # folder_struct_list.insert(0, base_folder_name)
        # upload_file_name = folder_struct_list.pop()
        # print(f"folder_struct_list is {folder_struct_list}")

        cli_open(folder_struct_list, upload_file_name, file_path)
        end_time = time.time()
        print(end_time - start_time)

    elif file_path.is_dir():
        typer.echo("is a directory")
    elif not file_path.exists():
        typer.echo("The file doesn't exist")


@app.command()
def pull(file_path: Path = typer.Argument(
    ...,
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)):
    """
    Replace local ipynb with (Remote)ipynb in google colab
    """
    start_time = time.time()
    if file_path is None:
        typer.echo("No file")
        raise typer.Abort()
    if file_path.is_file():
        start_time = time.time()
        git_root_path = get_git_root(file_path)

        base_folder_name = os.path.basename(git_root_path)
        rel_path = os.path.relpath(file_path, git_root_path)

        file_rel_path = os.path.join(base_folder_name, rel_path)
        folder_rel_path = os.path.dirname(file_rel_path)
        path_array_obj = Path(folder_rel_path)
        folder_struct_list = path_array_obj.parts
        upload_file_name = os.path.basename(file_path)
        print(upload_file_name)
        print(folder_struct_list)

        start_time = time.time()

        cli_pull(folder_struct_list, upload_file_name, file_path)
        end_time = time.time()
        print(end_time - start_time)

    elif file_path.is_dir():
        typer.echo("is a directory")
    elif not file_path.exists():
        typer.echo("The file doesn't exist")


@app.command()
def update(file_path: Path = typer.Argument(
    ...,
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)):
    """
    Replace (Remote)ipynb in google colab with local ipynb
    """
    start_time = time.time()
    if file_path is None:
        typer.echo("No file")
        raise typer.Abort()
    if file_path.is_file():
        start_time = time.time()
        git_root_path = get_git_root(file_path)

        base_folder_name = os.path.basename(git_root_path)
        rel_path = os.path.relpath(file_path, git_root_path)

        file_rel_path = os.path.join(base_folder_name, rel_path)
        folder_rel_path = os.path.dirname(file_rel_path)
        path_array_obj = Path(folder_rel_path)
        folder_struct_list = path_array_obj.parts
        upload_file_name = os.path.basename(file_path)
        print(upload_file_name)
        print(folder_struct_list)

        start_time = time.time()

        cli_update(folder_struct_list, upload_file_name, file_path)
        end_time = time.time()
        print(end_time - start_time)

    elif file_path.is_dir():
        typer.echo("is a directory")
    elif not file_path.exists():
        typer.echo("The file doesn't exist")
