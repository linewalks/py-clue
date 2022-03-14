from .cohort import CohortFeatures
from .comparison import CohortComparisonFeatures


class FeatureAdapter(
    CohortFeatures,
    CohortComparisonFeatures
):
  pass
