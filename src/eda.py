def summary_statistics(df):
    print("Number of rows:", len(df))
    print(df["vap_event"].value_counts())
    print(df["trial_arm_num"].value_counts())
    print(df["followup_days"].describe())

