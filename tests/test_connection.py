import pytest

from pyclue import CLUE


@pytest.mark.first
class TestConnection:
  def test_no_server(self):
    with pytest.raises(ConnectionError):
      clue = CLUE("server.dont.exists", 9999, "anyuser", "password")
      clue.connect()

  def test_wrong_username(self, clue_host, clue_port, clue_password):
    with pytest.raises(ConnectionRefusedError):
      clue = CLUE(
          clue_host,
          clue_port,
          "user!dont@exists#for$sure%",
          clue_password
      )
      clue.connect()

  def test_wrong_password(self, clue_host, clue_port, clue_username):
    with pytest.raises(ConnectionRefusedError):
      clue = CLUE(
          clue_host,
          clue_port,
          clue_username,
          "wrongpassword hahaha"
      )
      clue.connect()

  def test_success(slef, clue_host, clue_port, clue_username, clue_password):
    clue = CLUE(
        clue_host,
        clue_port,
        clue_username,
        clue_password
    )
    assert clue.connect()
