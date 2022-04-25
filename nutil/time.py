
import time
from time import strftime
import contextlib
import numpy as np


def sleep(s):
    time.sleep(s)


def ping():
    """Generate a time value to be later used by pong."""
    return time.time() * 1000


def pong(ping_, ms_rounding=3):
    """Returns the time delta in ms."""
    return round((time.time() * 1000) - ping_, ms_rounding)


@contextlib.contextmanager
def pingpong(desc='Pingpong', show=True, return_elapsed=None, ms_rounding=3):
    """A context manager to record elapsed time of execution of a code block."""
    p = ping()
    yield p
    elapsed = pong(p, ms_rounding)
    if show:
        print(f'{desc} elapsed in {elapsed}ms')
    if callable(return_elapsed):
        return_elapsed(elapsed)


@contextlib.contextmanager
def ratecounter(r):
    """A context manager to record elapsed time of execution of a code block, using a RateCounter object."""
    p = r.ping()
    yield p
    elapsed = r.pong()
    return elapsed


class RateCounter:
    """A simple rate counter (e.g. for FPS)"""

    def __init__(self, sample_size=120, starting_elapsed=1000):
        super().__init__()
        self.last_count = ping()
        self.__sample_size = sample_size
        self.sample = np.ones(self.sample_size, dtype=np.float64) * starting_elapsed
        self.__sample_index = 0

    @property
    def sample_size(self):
        return self.__sample_size

    def ping(self):
        self.last_count = ping()

    def pong(self):
        return self.tick()

    def start(self):
        self.last_count = ping()

    def tick(self):
        p = pong(self.last_count)
        self.last_count = ping()
        self.__sample_index = (self.__sample_index + 1) % self.sample_size
        self.sample[self.__sample_index] = p
        return p

    @property
    def rate(self):
        return 1000 / self.mean_elapsed_ms

    @property
    def rate_ms(self):
        return 1 / self.mean_elapsed_ms

    @property
    def mean_elapsed(self):
        return np.mean(self.sample) / 1000

    @property
    def mean_elapsed_ms(self):
        return np.mean(self.sample)

    @property
    def current_elapsed(self):
        return pong(self.last_count) / 1000

    @property
    def current_elapsed_ms(self):
        return pong(self.last_count)

    @property
    def last_elapsed(self):
        return self.sample[-1] / 1000

    @property
    def last_elapsed_ms(self):
        return self.sample[-1]

    @property
    def timed_block(self):
        return ratecounter(self)
