import pytest

from pyclue import CLUE


def pytest_addoption(parser):
  parser.addini("clue_host", "clue host", default="localhost")
  parser.addini("clue_port", "clue port", default="9999")
  parser.addini("clue_username", "clue username")
  parser.addini("clue_password", "clue password")
  parser.addini("test_cohort_id", "test cohort id")
  parser.addini("test_comparison_id", "test comparison id")
  parser.addini("test_incidence_rate_id", "test incidence rate id")


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


@pytest.fixture(scope="class")
def conn(clue):
  yield clue.connect()


@pytest.fixture(scope="session")
def test_cohort_id(request):
  return int(request.config.getini("test_cohort_id"))


@pytest.fixture(scope="session")
def test_comparison_id(request):
  return int(request.config.getini("test_comparison_id"))

@pytest.fixture(scope="session")
def test_incidence_rate_id(request):
  return int(request.config.getini("test_incidence_rate_id"))
