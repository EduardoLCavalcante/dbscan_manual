import pandas as pd
from src.algorithms.dbscan_manual import DBSCANManual
from src.datasets.load_datasets import load_iris_dataset
from src.visualization.plots import plot_dbscan_2d, plot_dbscan_3d

def run_iris():
    X, y, target_names = load_iris_dataset()

    X_3d = X[:, [0, 2, 3]]  # Sepal Length, Petal Length, Petal Width

    dbscan = DBSCANManual(eps=0.6, min_samples=5)
    dbscan.fit(X_3d)

    # 2D
    plot_dbscan_2d(
        X_3d[:, :2],
        dbscan.point_types_,
        title="DBSCAN Manual - Iris (2D)",
        filename="iris_2d_dbscan.png",
        xlabel="Sepal Length",
        ylabel="Petal Length"
    )

    # 3D
    plot_dbscan_3d(
        X_3d,
        dbscan.point_types_,
        title="DBSCAN Manual - Iris (3D)",
        filename="iris_3d_dbscan.png"
    )

    df = pd.DataFrame({
        "Classe Real": [target_names[i] for i in y],
        "Cluster DBSCAN": dbscan.labels_,
        "Tipo do Ponto": dbscan.point_types_
    })

    print(df.head(10))

if __name__ == "__main__":
    run_iris()
