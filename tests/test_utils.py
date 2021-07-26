from sequanix.utils import *
import pytest

from . import test_dir

def test_oncluster():
    assert on_cluster() is False

def test_rest2html():
    data = rest2html("""Test\n - text""").decode()
    assert "<li>text</li>" in data




def test_yamldocparser():
    r = YamlDocParser(f"{test_dir}/resources/test_generic_config.yml")
    assert r.sections == {'N': '# example of docstring\n', 'dummy': ''}
    assert r._block2docstring("N") == 'example of docstring'
    assert r._block2docstring("dummy") == ''

    r._block2docstring("notfound")


    # this test is a real-test example to etst _get_specials methods 
    r = YamlDocParser(f"{test_dir}/resources/test_complex_config.yml")
    assert r._get_specials("cutadapt") ==  {'tool_choice': ['atropos', 'cutadapt', 'fastp']}








