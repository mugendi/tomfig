"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from tomfig import Config
# init
# will search cwd/config
config = Config()


def test_str():
    assert "localhost:3000/development" in f"{config}"


def test_dot_access():
    assert config.data.APP.name == "My App"


def test_get_access():
    assert config.get("SERVER.API.domain") == "localhost:3000/development"


def test_missing_key_access():
    
    try:
        config.get("SERVER.API.port")
    except Exception as e:
        assert e.args[0] == "SERVER.API.port does not exist!"


if __name__ == "__main__":
    print(config.data.APP.nn)
