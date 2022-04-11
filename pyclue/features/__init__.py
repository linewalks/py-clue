from .cohort import CohortFeatures
from .comparison import CohortComparisonFeatures
from .incidence_rate import IncidencerateFeatures


class FeatureAdapter(
    CohortFeatures,
    CohortComparisonFeatures,
    IncidencerateFeatures
):
  pass
