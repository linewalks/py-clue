


class TestCohort:
  def test_cohort_list(self, conn):
    cohort_list = conn.get_cohort_list()
    assert isinstance(cohort_list, list)
