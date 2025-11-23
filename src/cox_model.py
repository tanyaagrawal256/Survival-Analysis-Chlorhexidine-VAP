from lifelines import CoxPHFitter
import matplotlib.pyplot as plt
import pandas as pd


def fit_cox_model(df: pd.DataFrame) -> CoxPHFitter:
    """
    Fit a Cox PH model with:
    - trial_arm_num (0 = 0.12%, 1 = 0.20%)
    - Age
    - APACHE II Score

    Returns the fitted CoxPHFitter object.
    """
    cols = ["followup_days", "vap_event", "trial_arm_num", "Age", "APACHE II Score"]
    cox_df = df[cols].dropna()

    cph = CoxPHFitter()
    cph.fit(cox_df, duration_col="followup_days", event_col="vap_event")
    return cph


def plot_cox_forest(cph: CoxPHFitter) -> None:
    """
    Plot log hazard ratios with 95% confidence intervals
    (forest-style plot).
    """
    cph.plot()
    plt.title("Cox Model – Log Hazard Ratios")
    plt.xlabel("log(HR) (95% CI)")
    plt.tight_layout()
    plt.show()

