from typing import List
from clue_pb2 import (
    RequestCohortList,
    RequestCohortStream
)

from pyclue.converter import convert
from pyclue.stream import Stream


class CohortFeatures:
  @convert()
  def get_cohort_list(
      self,
      page: int = 1,
      length: int = 0,
      term: str = ""
  ) -> List[dict]:
    """
    Get the list of cohorts.

    :param int page:
      Page number.
    :param int length:
      Number of cohorts in a page. If 0, all cohorts will be returned.
    :param str term:
      Search term.

    :return: List of cohorts.
    :rtype: List of dictionaries.
    """
    print("Get Cohort List")
    cohort_list = self.stub.GetCohortList(RequestCohortList(
        term=term,
        page=page,
        length=length,
    )).cohort_list

    return cohort_list

  def get_cohort_person_table(self, cohort_id: int) -> Stream:
    """
    Get person table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortPersonTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_person_table(self, cohort_id: int) -> Stream:
    """
    Get person table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortPersonTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_condition_occurrence_table(self, cohort_id: int) -> Stream:
    """
    Get condition_occurrence table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortConditionOccurrenceTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_death_table(self, cohort_id: int) -> Stream:
    """
    Get death table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortDeathTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_device_exposure_table(self, cohort_id: int) -> Stream:
    """
    Get device_exposure table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortDeviceExposureTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_drug_exposure_table(self, cohort_id: int) -> Stream:
    """
    Get drug_exposure table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortDrugExposureTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_measurement_table(self, cohort_id: int) -> Stream:
    """
    Get measurement table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortMeasurementTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_observation_period_table(self, cohort_id: int) -> Stream:
    """
    Get observation_period table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortObservationPeriodTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_observation_table(self, cohort_id: int) -> Stream:
    """
    Get observation table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortObservationTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_procedure_occurrence_table(self, cohort_id: int) -> Stream:
    """
    Get procedure_occurrence table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortProcedureOccurrenceTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )

  def get_cohort_visit_occurrence_table(self, cohort_id: int) -> Stream:
    """
    Get visit_occurrence table of a cohort.
    Data stream connection will be opened.

    :param int cohort_id:
      ID of the cohort.

    :return: Stream object.
    :rtype: Stream
    """
    return Stream(
        self.stub.GetCohortVisitOccurrenceTable,
        RequestCohortStream,
        cohort_id=cohort_id
    )
