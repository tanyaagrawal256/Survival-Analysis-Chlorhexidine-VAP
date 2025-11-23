import pandas as pd

def load_and_clean_data(path):
    df = pd.read_excel(path)

    df["vap_event"] = df["Outcome of the current episode"].apply(
        lambda x: 1 if str(x).strip().lower() == "vap" else 0
    )

    df["trial_arm_num"] = df["Trial Arm"].map({"Group 1": 0, "Group 2": 1})

    df["followup_days"] = df["Day 1"]

    return df

