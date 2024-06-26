# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V63q-UG-mwN6Mi96bS4MZ2AmUTHYo_ri
"""

import numpy as np

class NearestNeighbor:
  def __init__(self,k):
    self.k = k
  def train(self,X,y):
    self.Xtr = X
    self.ytr = y

  def predict(self, X):
    num_test = X.shape[0]
    Ypred_l1 = np.zeros(num_test, dtype = self.ytr.dtype)
    Ypred_l2 = np.zeros(num_test, dtype = self.ytr.dtype)

    for i in range(num_test):
      k_range_ls = []
      distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
      distances_index = distances.argsort()
      Ypred_l1_all= self.ytr[distances_index[:self.k]]
      t_l1, cnt = np.unique(Ypred_l1_all, return_counts = True)
      Ypred_l1[i] = t_l1[np.argmax(cnt)]
    for i in range(num_test):
      k_range_ls = []
      distances = np.sum(np.sqrt((self.Xtr - X[i,:])**2), axis = 1)
      distances_index = distances.argsort()
      Ypred_l2_all = self.ytr[distances_index[:self.k]]
      t_l2, cnt = np.unique(Ypred_l2_all, return_counts = True)
      Ypred_l2[i] = t_l2[np.argmax(cnt)]

    return Ypred_l1, Ypred_l2

