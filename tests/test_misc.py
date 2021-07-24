from sequanix.misc import *

def test_oncluster():
    assert on_cluster() is False
    import platform
    name = platform.uname().node 
    assert on_cluster([name]) is True
    assert on_cluster(name) is True

def test_rest2html():
    data = rest2html("""Test\n - text""").decode()
    assert "<li>text</li>" in data
