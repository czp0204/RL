import numpy as np
import tensorflow as tf
import pandas as pd

np.random.seed(1)
tf.compat.v1.set_random_seed(1)

# deep q network off-policy


class DeepQNetwork:
    def __init__(self,
                 n_actions,
                 n_features,
                 learning_rate=0.1,
                 reward_decay=0.9,
                 e_greedy=0.9, # 九成选择q大的situation
                 replace_target_iter=300,  # 隔了多少更新一次
                 memory_size=500,  # 记录多少条信息
                 batch_size =32,  # 随机梯度下降
                 e_greedy_increasement=None,
                 output_graph=False):
        self.n_actions = n_actions
        self.memory_size = memory_size  # pandas的使用
        self.memory = pd.DataFrame(np.zeros(self.memory_size, n_features*2+2))


'''
    config of layers
    tf.matmul 是干啥的
    建立两个结构相同 但是参数不同的网络
    '''


def build_net(self):
    pass


def store_transition(self, s, a, r, s_):
    pass


def choose_action(self, observation):
    pass
#  把参数放到q现实里


def _replace_target_params(self):
    e_params = tf.compat.v1.assign()
    t_params = tf.compat.v1.get_collection('')
    self.sess.run(tf.compat.v1.assign(t, e) for t, e in zip(t_params, e_params))
    # 对于每一个e and t都进行zip


def learn(self):
    pass


def plot_cost(self):
    pass
