import pytest

from smartva.utils import utils


def test_shorten_path():
    path = r'C:\Development\smartva\data\verbal_autopsy.csv'
    assert utils.shorten_path(path, 20) == r'C:\De...bal_autopsy.csv'


def test_find_dupes():
    dupes = ['test1', 'test2', 'test1', 'test3']
    assert utils.find_dupes(dupes) == ['test1']


def test_int_or_float():
    assert utils.int_or_float('1') == 1
    assert utils.int_or_float('1.1') == 1.1
    with pytest.raises(ValueError):
        utils.int_or_float('1 2')
