import matplotlib.pyplot as plt


def save_current_plot(path: str) -> None:
    """Save the current Matplotlib figure to the given path."""
    plt.savefig(path, dpi=300, bbox_inches="tight")

