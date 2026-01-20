import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FIGURES_DIR = "reports/figures"

def _ensure_dir():
    os.makedirs(FIGURES_DIR, exist_ok=True)

def plot_dbscan_2d(
    X,
    point_types,
    title,
    filename,
    xlabel="X1",
    ylabel="X2"
):
    _ensure_dir()

    colors = {
        'core': 'blue',
        'border': 'orange',
        'noise': 'red'
    }

    plt.figure(figsize=(8, 6))

    for p_type in ['core', 'border', 'noise']:
        idx = point_types == p_type
        plt.scatter(
            X[idx, 0],
            X[idx, 1],
            c=colors[p_type],
            label=p_type.capitalize(),
            alpha=0.7,
            edgecolors='k'
        )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)

    # Salva a figura
    plt.savefig(
        os.path.join(FIGURES_DIR, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def plot_dbscan_3d(
    X,
    point_types,
    title,
    filename
):
    _ensure_dir()

    colors = {
        'core': 'blue',
        'border': 'orange',
        'noise': 'red'
    }

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')

    for p_type in ['core', 'border', 'noise']:
        idx = point_types == p_type
        ax.scatter(
            X[idx, 0],
            X[idx, 1],
            X[idx, 2],
            c=colors[p_type],
            label=p_type.capitalize(),
            alpha=0.7
        )

    ax.set_title(title)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_zlabel("Feature 3")
    ax.legend()

    # Salva a figura
    plt.savefig(
        os.path.join(FIGURES_DIR, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()
