import pytest


class TestCohort:
  @pytest.fixture(scope="session")
  def test_table_name(self, request):
    return request.config.getini("test_table_name")

  def test_cohort_list(self, conn):
    cohort_list = conn.get_cohort_list()
    assert isinstance(cohort_list, list)

  def test_table_list(self, conn):
    table_list = conn.get_cohort_table_list()
    assert isinstance(table_list, list)
    assert table_list

  def test_table_data(self, conn, test_cohort_id, test_table_name):
    result = conn.get_cohort_table(
        test_cohort_id,
        test_table_name
    )
    obj = result.fetchone()
    assert obj

  def test_table_data_fetchmany(self, conn, test_cohort_id, test_table_name):
    result = conn.get_cohort_table(
        test_cohort_id,
        test_table_name
    )
    obj_list = result.fetchmany(10)
    assert obj_list
