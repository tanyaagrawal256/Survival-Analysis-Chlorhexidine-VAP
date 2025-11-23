import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def run_eda(df: pd.DataFrame) -> None:
    """Print basic EDA and show barplot of events by treatment group."""

    print("Number of patients:", len(df))

    print("\nTrial arm counts:")
    print(df["trial_arm"].value_counts())

    print("\nVAP events overall:")
    print(df["vap_event"].value_counts())

    print("\nFollow-up days summary:")
    print(df["followup_days"].describe())

    # Barplot of VAP events by treatment group
    plt.figure(figsize=(6, 4))
    sns.countplot(x="trial_arm", hue="vap_event", data=df)
    plt.title("VAP events by treatment group")
    plt.xlabel("Chlorhexidine concentration")
    plt.ylabel("Number of patients")
    plt.legend(labels=["No VAP (0)", "VAP (1)"])
    plt.tight_layout()
    plt.show()
