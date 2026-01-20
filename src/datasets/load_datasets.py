from sklearn.datasets import make_moons, make_circles, load_iris

def load_moons():
    X, y = make_moons(
        n_samples=300,
        noise=0.08,
        random_state=42
    )
    return X, y

def load_circles():
    X, y = make_circles(
        n_samples=300,
        factor=0.5,
        noise=0.05,
        random_state=42
    )
    return X, y

def load_iris_dataset():
    iris = load_iris()
    return iris.data, iris.target, iris.target_names
