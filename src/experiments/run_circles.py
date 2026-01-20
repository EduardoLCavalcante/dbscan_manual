from src.algorithms.dbscan_manual import DBSCANManual
from src.datasets.load_datasets import load_circles
from src.visualization.plots import plot_dbscan_2d

def run_circles():
    X, _ = load_circles()

    dbscan = DBSCANManual(eps=0.2, min_samples=5)
    dbscan.fit(X)

    plot_dbscan_2d(
        X,
        dbscan.point_types_,
        title="DBSCAN Manual - Two Circles",
        filename="two_circles_dbscan.png"
    )

if __name__ == "__main__":
    run_circles()
