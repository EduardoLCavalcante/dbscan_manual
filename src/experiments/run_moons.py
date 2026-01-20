from src.algorithms.dbscan_manual import DBSCANManual
from src.datasets.load_datasets import load_moons
from src.visualization.plots import plot_dbscan_2d

def run_moons():
    X, _ = load_moons()

    dbscan = DBSCANManual(eps=0.25, min_samples=5)
    dbscan.fit(X)

    plot_dbscan_2d(
        X,
        dbscan.point_types_,
        title="DBSCAN Manual - Two Moons",
        filename="two_moons_dbscan.png"
    )

if __name__ == "__main__":
    run_moons()
