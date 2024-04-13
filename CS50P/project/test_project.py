from cryptography.fernet import Fernet
import os
import pytest
from project import load_key, add, view


@pytest.fixture
def key_file(tmp_path):
    key = Fernet.generate_key()
    key_path = tmp_path / "key.key"
    with open(key_path, 'wb') as f:
        f.write(key)
    yield key_path


@pytest.fixture
def password_file(tmp_path):
    password_path = tmp_path / "password.txt"
    yield password_path


def test_load_key(key_file):
    assert os.path.isfile(key_file)
    key = load_key()
    assert isinstance(key, bytes)


def test_add(password_file, key_file, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'test_user\nTestPassword123')
    add()
    with open(password_file, 'r') as f:
        assert len(f.readlines()) == 1


def test_view(password_file, key_file, monkeypatch, capsys):
    with open(password_file, 'w') as f:
        f.write('test_user|encrypted_password\n')
    monkeypatch.setattr('builtins.input', lambda _: 'view')
    view()
    captured = capsys.readouterr()
    assert 'test_user' in captured.out
    assert 'encrypted_password' not in captured.out  # Ensure that decrypted password is not printed

