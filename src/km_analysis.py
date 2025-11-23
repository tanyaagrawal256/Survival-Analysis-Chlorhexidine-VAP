import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
import pandas as pd


def km_overall(df: pd.DataFrame) -> None:
    """Overall KM curve (all patients together)."""
    kmf = KaplanMeierFitter()

    kmf.fit(df["followup_days"], event_observed=df["vap_event"], label="Overall Survival")

    plt.figure(figsize=(8, 5))
    kmf.plot_survival_function(ci_show=True)
    plt.title("Overall Kaplan–Meier VAP-free Survival")
    plt.xlabel("Follow-up time (days)")
    plt.ylabel("Probability of remaining VAP-free")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def km_by_trial_arm(df: pd.DataFrame) -> None:
    """KM curves by chlorhexidine concentration (0.12% vs 0.20%)."""
    kmf = KaplanMeierFitter()

    plt.figure(figsize=(8, 6))

    for label, group_data in df.groupby("trial_arm"):
        kmf.fit(
            durations=group_data["followup_days"],
            event_observed=group_data["vap_event"],
            label=label,
        )
        kmf.plot_survival_function(ci_show=True)

    plt.title("Kaplan–Meier VAP-free Survival by Chlorhexidine Concentration")
    plt.xlabel("Follow-up time (days)")
    plt.ylabel("Probability of remaining VAP-free")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

