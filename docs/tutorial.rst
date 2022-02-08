Basic Tutorial
==============

.. code-block:: python

  clue = CLUE("localhost", 9999, "test@linewalks.com", "password")
  conn = clue.connect()

  cohort_list = conn.get_cohort_list(page=1, length=10)

  result = conn.get_cohort_person_table(cohort_id=123)
  result.fetchone()
  result.fetchmany(10)
