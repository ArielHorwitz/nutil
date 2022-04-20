
import logging
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


import os, sys
import numpy as np
from pathlib import Path


class List:
    @staticmethod
    def move_top(l: list, index: int):
        """
        Bump an item to the top of a list in place (without copying).

        :param l:       List
        :param index:   Index int
        :return:        Same list
        """
        item = l.pop(index)
        new_index = 0
        l.insert(new_index, item)
        return new_index

    @staticmethod
    def move_up(l: list, index: int):
        """
        Bump an item up once in a list in place (without copying).

        :param l:       List
        :param index:   Index int
        :return:        Same list
        """
        item = l.pop(index)
        new_index = index - 1 if index > 0 else index
        l.insert(new_index, item)
        return new_index

    @staticmethod
    def move_down(l: list, index: int):
        """
        Bump an item down once in a list in place (without copying).

        :param l:       List
        :param index:   Index int
        :return:        Same list
        """
        item = l.pop(index)
        new_index = index + 1 if index < len(l) else index
        l.insert(new_index, item)
        return new_index

    @staticmethod
    def move_bottom(l: list, index: int):
        """
        Bump an item to the bottom of a list in place (without copying).

        :param l:       List
        :param index:   Index int
        :return:        Same list
        """
        item = l.pop(index)
        new_index = len(l)
        l.insert(new_index, item)
        return new_index

    @staticmethod
    def swap(l: list, index1: int, index2: int):
        """
        Swap the position of two items of a list in place (without copying).

        :param l:       List
        :param index1:  First index
        :param index2:  Second index
        """
        a = l[index1]
        b = l[index2]
        l[index2] = a
        l[index1] = b


def restart_script():
    m = 'Restarting python script...'
    print(m)
    logger.info(m)
    os.execl(sys.executable, sys.executable, *sys.argv)

def configure_logging(file=None, level=None, datefmt=None):
    file = Path.cwd() / 'debug.log'
    if file.is_file():
        file.unlink()
    level = logging.DEBUG if level is None else level
    datefmt = '%Y-%m-%d %H:%M:%S.%f' if datefmt is None else datefmt
    logging.basicConfig(level=level, filename=file, datefmt=datefmt)
    m = f'Configured debug Log at: {file} (log level: {level})\n'
    print(m)
    logger.info(m)

def normalize(a, size=1):
    v_size = np.linalg.norm(a, axis=-1)
    if v_size == 0:
        return np.array(a) * 0
    return np.array(a) * size / v_size

def str2int(s):
    v = 0
    for i, char in enumerate(reversed(s)):
        v += max(ord(char)*(130**i), 130)
    return v

def decimal2hex(n):
    return f"{hex(int(n*255)).split('x')[-1]:0>2}"

def is_floatable(n):
    try:
        float(n)
        return True
    except (ValueError, TypeError):
        return False

def is_intable(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def try_float(v):
    try:
        return float(v)
    except ValueError:
        return v

def is_iterable(v, count_string=True):
    if not count_string and isinstance(v, str):
        return False
    try:
        v.__iter__()
        return True
    except AttributeError:
        return False

def minmax(minimum, maximum, value):
    assert minimum <= maximum
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    return value

def nsign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

def nsign_str(n):
    if n >= 0:
        return f'+{n}'
    return str(n)

def sortable_timestamp():
    """
    Return a string-sortable timestamp.

    :return:    Formatted timestamp
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
