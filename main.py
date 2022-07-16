import numpy as np
from Model import Model
from scipy.stats import poisson
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from matplotlib.patches import Patch

def read_S(filename):
    with open(filename) as f:
        lines = f.readlines()

    lambdas = []
    for elem in lines:
        one = elem.strip()
        lambdas.append(float(one))

    return np.array(lambdas)

def read_coords(filename):
    with open(filename) as f:
        lines = f.readlines()

    coords = []
    for elem in lines:
        one, two = elem.strip().split()
        coords.append([float(one), float(two)])

    return np.array(coords)

def compute_point_colors(final_labels, colors):
    final_colors = []
    for elem in final_labels:
        final_colors.append(colors[elem])

    return final_colors

def plot_poisson(num_clusters, S, model, colors, final_colors):

    for i in range(num_clusters):
        x = np.arange(-1, 30, 1)
        poisson_rv = poisson(mu=model.lambdas[i])
        color = colors[i]
        plt.plot(poisson_rv.pmf(x), color=color)
    y = [0] * 100
    plt.scatter(S, y, color=final_colors)
    plt.legend()
    plt.show()

def plot_contour_guassians(num_clusters, X, model, colors, final_colors):

    fig, ax = plt.subplots()
    for i in range(num_clusters):
        x = np.linspace(-2, 10, 500)
        y = np.linspace(-3, 10, 500)
        F, Y = np.meshgrid(x, y)
        pos = np.empty(F.shape + (2,))
        pos[:, :, 0] = F
        pos[:, :, 1] = Y
        color = colors[i]
        normal = multivariate_normal(mean=model.mu[i], cov=model.sigma[i])
        ax.contour(F, Y, normal.pdf(pos), colors=color, alpha=0.4)

    ax.scatter(X[:, 0], X[:, 1], c=final_colors, cmap='Accent')
    pa1 = Patch(facecolor='red', edgecolor='black')
    pa2 = Patch(facecolor='blue', edgecolor='black')
    pa3 = Patch(facecolor='green', edgecolor='black')
    pb1 = Patch(facecolor='purple', edgecolor='black')
    pb2 = Patch(facecolor='black', edgecolor='black')

    clusters = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
    pas = [pa1, pa2, pa3, pb1, pb2]
    ax.legend(handles=[pas[i] for i in range(num_clusters)],
              labels=[clusters[i] for i in range(num_clusters)],
              ncol=1, handletextpad=0.5, handlelength=2.0, columnspacing=-0.5,
              loc='upper right', fontsize=8)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def main():
    X = read_coords('X.txt')
    S = read_S('S.txt')
    num_clusters = 3
    model = Model(num_clusters)
    model.fit(X, S)
    final_labels = model.predict()
    colors = ['red', 'blue', 'green', 'purple', 'black']
    final_colors = compute_point_colors(final_labels, colors)
    plot_poisson(num_clusters, S, model, colors, final_colors)
    plot_contour_guassians(num_clusters, X, model, colors, final_colors)

if __name__ == '__main__':
    main()
