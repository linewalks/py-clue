from clue_pb2 import (
    RequestCohortList,
    RequestCohortStream
)

from pyclue.converter import convert
from pyclue.stream import Stream


class CohortFeatures:
  @convert()
  def get_cohort_list(self, page=1, length=0, term=""):
    cohort_list = self.stub.GetCohortList(RequestCohortList(
        term=term,
        page=page,
        length=length,
    )).cohort_list

    return cohort_list

  def get_cohort_person_table(self, cohort_id):
    return Stream(
        self.stub.GetCohortPersonTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )
