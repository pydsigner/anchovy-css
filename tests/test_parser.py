import pathlib

import pytest

from anchovy_css.parser import process


TEST_CASES = pathlib.Path(__file__).parent / 'cases'


def load_case(name: str):
    acss = (TEST_CASES / name).with_suffix('.anchovy.css')
    expected = (TEST_CASES / name).with_suffix('.css')
    return acss.read_text('utf-8'), expected.read_text('utf-8')


@pytest.mark.parametrize('acss,expected', [
    load_case('appended_class'),
    load_case('fanout_nesting'),
    load_case('import'),
    load_case('media_query'),
    load_case('multi_selector'),
    load_case('nested_media'),
    load_case('pseudoclass'),
    load_case('simple_class'),
])
def test_process(acss, expected):
    assert process(acss) == expected
