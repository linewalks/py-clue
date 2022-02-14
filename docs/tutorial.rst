Basic Tutorial
==============

Basic Usage
***********

.. code-block:: python

  from pyclue import CLUE
  clue = CLUE("localhost", 9999, "test@linewalks.com", "password")
  conn = clue.connect()

  cohort_list = conn.get_cohort_list(page=1, length=10)

  result = conn.get_cohort_person_table(cohort_id=123)
  one_person = result.fetchone()
  person_list =result.fetchmany(10)


With Pandas
***********

.. code-block:: python

  from pandas as pd
  result = conn.get_cohort_person_table(cohort_id=123)
  df = pd.DataFrame(result.fetchall())
