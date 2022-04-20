
import logging
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

from pathlib import Path
import os
import shutil
import platform
import subprocess

CWD = Path.cwd()


def give_usr_dir(dir_name):
    """
    Create and give a directory path in the user's local home directory according to the OS (NT or posix).

    :param dir_name:    Directory name
    :return:            Path to directory (pathlib.Path object)
    """
    path = Path.home()
    if os.name == 'posix':
        path = path / '.local' / 'share' / f'{dir_name.lower()}'
    elif os.name == 'nt':
        path = path / 'AppData' / 'Local' / f'{dir_name.capitalize()}'
    else:
        raise NotImplementedError(f'Unknown OS ({os.name})')
    if not path.is_dir():
        path.mkdir()
    return path

def file_dump(file, d, clear=True):
    with open(file, 'w' if clear else 'a') as f:
        f.write(d)

def file_load(file):
    with open(file, 'r') as f:
        d = f.read()
    return d

def file_copy(src, dst, *a, **k):
    return shutil.copy(src, dst, *a, **k)

def file_move(src, dst, *a, **k):
    return shutil.move(src, dst, *a, **k)

def archive(src, name, dst=None, format='zip'):
    assert isinstance(src, Path)
    dst = src.parent if dst is None else dst
    archive_file_noext = dst / name
    shutil.make_archive(
        str(archive_file_noext),
        format=format,
        root_dir=src.parent,
        base_dir=src.name
    )

def open_file_explorer(path=None):
    if path is None:
        path = CWD
    if platform.system() == 'Windows':
        os.startfile(path)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', path])
    else:
        subprocess.Popen(['xdg-open', path])
