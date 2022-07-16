import numpy as np
from scipy.stats import multivariate_normal
from scipy.stats import poisson
import random

class Model:
    def __init__(self, k, max_iter=50):
        self.k = k
        self.max_iter = int(max_iter)

    def initialize(self, X):
        self.shape = X.shape
        self.n, self.m = self.shape
        self.pi = [1/self.k]*self.k
        self.gamma = [[0] * self.k for i in range(self.n)]
        secure_random = random.SystemRandom()
        self.mu = [[secure_random.uniform(0, 10), secure_random.uniform(0, 10)] for _ in range(self.k)]
        self.sigma = [[1, 1] for _ in range(self.k)]
        self.lambdas = [secure_random.uniform(0, 20) for _ in range(self.k)]

    def e_step(self, X, S):
        self.gamma = self.evaluate_responsibilities(X, S)

    def m_step(self, X, S):
        self.pi = self.gamma.mean(axis=0)
        for i in range(self.k):
            weight = self.gamma[:, [i]]
            total_weight = weight.sum()
            self.mu[i] = (X * weight).sum(axis=0) / total_weight

            self.sigma[i] = np.cov(X.T,
                                   aweights=(weight / total_weight).flatten(),
                                   bias=True)
            self.lambdas[i] = (S[i] * weight).sum(axis=0) / total_weight

    def evaluate_responsibilities(self, X, S):
        likelihood = np.zeros((self.n, self.k))
        for i in range(self.k):
            normal_pdf = multivariate_normal(
                mean=self.mu[i],
                cov=self.sigma[i])
            poisson_rv = poisson(mu=self.lambdas[i])
            likelihood[:, i] = normal_pdf.pdf(X)*poisson_rv.pmf(S)

        print(likelihood)
        numerator = likelihood * self.pi
        denominator = numerator.sum(axis=1)[:, np.newaxis]
        weights = numerator / denominator

        return weights

    def fit(self, X, S):
        self.initialize(X)
        for iteration in range(self.max_iter):
            self.e_step(X, S)
            self.m_step(X, S)

    def predict(self):

        return np.argmax(self.gamma, axis=1)
