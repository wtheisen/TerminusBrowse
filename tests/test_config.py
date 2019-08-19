import json, os, sys

from config import Config

import pytest

DEFAULT = os.path.expanduser('~') + '/.config/TerminusBrowser/config.json'
test_list = [
    ('', DEFAULT),
    ('/tmp/', DEFAULT),
    ('/tmp/cfg.json', '/tmp/cfg.json')
]

@pytest.mark.parametrize("test_input, expected", test_list)
def test_location(test_input, expected):
    assert Config(test_input).location == expected
