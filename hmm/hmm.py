import numpy as np
from . import util

class DiscreteHMM:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.__random_init_model()

    def __random_init_model(self):
        # Random assign value
        self.log_A = np.log(util.normalize2d(np.random.rand(self.N, self.N)))
        self.log_B = np.log(util.normalize2d(np.random.rand(self.N, self.M)))
        self.log_pi = np.log(util.normalize1d(np.random.rand(self.N)))

    def show_model(self):
        print('A: Transition probability'.center(70, '-'))
        print(np.exp(self.log_A))
        print('B: Emission probability'.center(70, '-'))
        print(np.exp(self.log_B))
        print('pi: initital state distribution'.center(70, '-'))
        print(np.exp(self.log_pi))

    def check_model(self):
        return abs(np.sum(np.exp(self.log_A)) - self.N) < util.EPS \
            and abs(np.sum(np.exp(self.log_B)) - self.N) < util.EPS \
            and abs(np.sum(np.exp(self.log_pi)) - 1.0) < util.EPS