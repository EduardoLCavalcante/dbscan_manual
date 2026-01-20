import numpy as np
from collections import deque

class DBSCANManual:
    """
    Implementação manual do algoritmo DBSCAN.
    Classifica explicitamente os pontos em:
    - core (núcleo)
    - border (borda)
    - noise (ruído)
    """

    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        self.labels_ = None
        self.point_types_ = None

    def _euclidean_distance(self, p1, p2):
        return np.linalg.norm(p1 - p2)

    def _region_query(self, X, idx):
        neighbors = []
        for i in range(len(X)):
            if self._euclidean_distance(X[idx], X[i]) <= self.eps:
                neighbors.append(i)
        return neighbors

    def fit(self, X):
        n = len(X)
        self.labels_ = np.full(n, -1)
        self.point_types_ = np.full(n, 'noise', dtype=object)

        visited = np.zeros(n, dtype=bool)
        cluster_id = 0

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            neighbors = self._region_query(X, i)

            if len(neighbors) < self.min_samples:
                self.point_types_[i] = 'noise'
            else:
                self._expand_cluster(X, i, neighbors, cluster_id, visited)
                cluster_id += 1

        return self

    def _expand_cluster(self, X, idx, neighbors, cluster_id, visited):
        self.labels_[idx] = cluster_id
        self.point_types_[idx] = 'core'

        queue = deque(neighbors)

        while queue:
            current = queue.popleft()

            if not visited[current]:
                visited[current] = True
                current_neighbors = self._region_query(X, current)

                if len(current_neighbors) >= self.min_samples:
                    self.point_types_[current] = 'core'
                    queue.extend(current_neighbors)
                else:
                    self.point_types_[current] = 'border'

            if self.labels_[current] == -1:
                self.labels_[current] = cluster_id
