from clue_pb2 import (
    RequestCohortList
)

from .converter import convert


class CohortFeatures:
  @convert()
  def get_cohort_list(self, page=1, length=0, term=""):
    cohort_list = self.stub.GetCohortList(RequestCohortList(
        term=term,
        page=page,
        length=length,
    )).cohort_list

    return cohort_list
