import pytest

from pyclue import CLUE


def pytest_addoption(parser):
  parser.addini("clue_host", "clue host", default="localhost")
  parser.addini("clue_port", "clue port", default="9999")
  parser.addini("clue_username", "clue username")
  parser.addini("clue_password", "clue password")


@pytest.fixture(scope="session")
def clue_host(request):
  return request.config.getini("clue_host")


@pytest.fixture(scope="session")
def clue_port(request):
  return request.config.getini("clue_port")


@pytest.fixture(scope="session")
def clue_username(request):
  return request.config.getini("clue_username")


@pytest.fixture(scope="session")
def clue_password(request):
  return request.config.getini("clue_password")


@pytest.fixture(scope="class")
def clue(clue_host, clue_port, clue_username, clue_password):
  return CLUE(
      clue_host,
      clue_port,
      clue_username,
      clue_password
  )
