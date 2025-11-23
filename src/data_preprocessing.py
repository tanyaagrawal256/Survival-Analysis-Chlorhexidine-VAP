import pandas as pd
import numpy as np
import re


def load_and_prepare_data(path: str) -> pd.DataFrame:
    """
    Load the Chlorhexidine Trial Excel file and create the main
    survival analysis variables:

    - followup_days: last day (1–10) where any 'Day N' column has data
    - vap_event: 1 if Outcome of the current episode == 'VAP', else 0
    - trial_arm: 'CHX 0.12%' or 'CHX 0.20%'
    - trial_arm_num: 0 for Group 1 (0.12%), 1 for Group 2 (0.20%)

    Returns a cleaned DataFrame.
    """

    # --- Step 1: Load data ---
    df = pd.read_excel(path)

    # --- Step 2: Build mapping of all "Day N" columns (N = 1..10) ---
    day_cols = {d: [] for d in range(1, 11)}

    for col in df.columns:
        m = re.search(r"Day (\d+)", col)
        if m:
            d = int(m.group(1))
            if d in day_cols:
                day_cols[d].append(col)

    # --- Step 3: For each row, find last day with ANY non-missing data ---
    def get_last_day(row):
        last = 0
        for d, cols in day_cols.items():
            if any(not pd.isna(row[c]) for c in cols):
                last = d
        return last

    df["followup_days"] = df.apply(get_last_day, axis=1)

    # Drop rows with no follow-up data
    df = df[df["followup_days"] > 0].copy()

    # --- Step 4: Event indicator (VAP yes/no) ---
    df["vap_event"] = (df["Outcome of the current episode"] == "VAP").astype(int)

    # --- Step 5: Treatment groups (0.12% vs 0.20%) ---
    df["trial_arm"] = df["Trial Arm"].map({
        "Group 1": "CHX 0.12%",
        "Group 2": "CHX 0.20%"
    })

    df["trial_arm_num"] = df["Trial Arm"].map({
        "Group 1": 0,   # 0.12%
        "Group 2": 1    # 0.20%
    })

    return df
