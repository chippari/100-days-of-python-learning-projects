# ----------------------------------------------------------------------------------------------------------------------
# > Day 26 - Learning about Iterrows in Pandas -------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-19
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd

# Pandas Iterrows:
# Iterate over DataFrame rows as (index, Series) pairs.

# Pandas Iterrows Structure:
# DataFrame.iterrows()

# Example:
student_dict = {
    "student": ["Fabio", "Isabela", "Valdomiro"],
    "score": [71, 92, 57]
}

student_df = pd.DataFrame(student_dict)

# Loop trough rows of a data frame.
for (index, row) in student_df.iterrows():
    print(row.student, row.score)

# ----------------------------------------------------------------------------------------------------------------------
