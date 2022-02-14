import pytest

class TestCohort:
  def test_cohort_list(self, conn):
    cohort_list = conn.get_cohort_list()
    assert isinstance(cohort_list, list)


class TestCohortPersonTable:
  @pytest.fixture(scope="function")
  def result(self, conn, test_cohort_id):
    stream = conn.get_cohort_person_table(test_cohort_id)
    yield stream
    stream.close()

  def test_fetchone(self, result):
    obj = result.fetchone()
    assert "person_id" in obj

  @pytest.mark.parametrize("num", [1, 2, 5, 10])
  def test_fetchmany(self, result, num):
    obj_list = result.fetchmany(num)
    assert isinstance(obj_list, list)
    assert len(obj_list) <= num

  def test_fetchall(self, result):
    obj_list = result.fetchall()
    assert isinstance(obj_list, list)

  def test_multiple(self, result):
    assert result.fetchone()
    assert result.fetchone()
    assert result.fetchmany(2)


class TestCohortTables:
  @pytest.mark.parametrize(
      "table_name",
      [
          "condition_occurrence",
          "death",
          "device_exposure",
          "drug_exposure",
          "measurement",
          "observation_period",
          "observation",
          "procedure_occurrence",
          "visit_occurrence"
      ]
  )
  def test_fetchone(self, conn, test_cohort_id, table_name):
    func = getattr(conn, f"get_cohort_{table_name}_table")
    stream = func(test_cohort_id)
    obj = stream.fetchone()
    assert "person_id" in obj
    stream.close()
