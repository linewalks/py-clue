# py-clue
The Python interface to the MDwalks CLUE.

#### Description

To be defined..


## Getting Started

#### Install
```sh
pip install python-clue
```

## Usage

#### Basic Usage

```python
from pyclue import CLUE
clue = CLUE(
    "localhost",  # CLUE server host
    9999,  # CLUE server port
    "test@linewalks.com",  # test account name
    "password"  # test account password
)
conn = clue.connect()

cohort_list = conn.get_cohort_list()

result = conn.get_cohort_person_table(123) # cohort_id: 123
person_list = result.fetchall()
```

#### With pandas
```python
import pandas as pd

result = conn.get_cohort_person_table(123)
df = pd.DataFrame(person_list)
```


## Contribution

To be defined...

## Contact

* Chae Jungwoo - jungwoo@linewalks.com
