from gui.core.create_json import readTxt
from pathlib import Path
from json import loads

def test_read_txt():
    output = readTxt("./tests/data/txt")
    expected = loads(Path("./tests/data/json.json").read_text())
    assert output == expected
