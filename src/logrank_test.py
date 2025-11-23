from lifelines.statistics import logrank_test
import pandas as pd


def logrank_by_trial_arm(df: pd.DataFrame):
    """
    Run a log-rank test comparing CHX 0.12% vs CHX 0.20%
    based on followup_days and vap_event.
    """
    group_012 = df[df["trial_arm"] == "CHX 0.12%"]
    group_020 = df[df["trial_arm"] == "CHX 0.20%"]

    results = logrank_test(
        group_012["followup_days"], group_020["followup_days"],
        event_observed_A=group_012["vap_event"],
        event_observed_B=group_020["vap_event"],
    )
    return results

