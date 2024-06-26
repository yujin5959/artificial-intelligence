# -*- coding: utf-8 -*-
"""Homework02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C1v2IsmhLdhOpvl3TQxeh-eJOMix6Ubo
"""

import numpy as np

def unpickle(file):
  import pickle
  with open(file, 'rb') as fo:
    dict = pickle.load(fo, encoding='bytes')
  return dict

test = unpickle('/content/drive/MyDrive/AI lab/data_batch_1')
print(type(test))

test.keys()

for item in test:
  print(item, type(test[item]))

set(test[b'labels'])

test[b'data']

np.shape(test[b'data'])

meta = unpickle('/content/drive/MyDrive/AI lab/batches.meta')

type(meta)
meta.keys()

meta[b'label_names']

import numpy as np
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/AI lab
!pwd

def unpickle(file):
  import pickle
  with open(file, 'rb') as fo:
    dict = pickle.load(fo, encoding ='bytes')
  return dict

bat1 = unpickle('data_batch_1')
bat2 = unpickle('data_batch_2')
bat3 = unpickle('data_batch_3')
bat4 = unpickle('data_batch_4')
bat5 = unpickle('data_batch_5')
bat_test = unpickle('test_batch')

data = np.concatenate([bat1[b'data'],bat2[b'data'],bat3[b'data'],bat4[b'data'],bat5[b'data']])
labels = np.concatenate([bat1[b'labels'],bat2[b'labels'],bat3[b'labels'],bat4[b'labels'],bat5[b'labels']])

np.shape(data)

np.shape(labels)

import matplotlib.pyplot as plt
img = data.reshape(50000,3,32,32)
img = img.transpose(0,2,3,1)
plt.imshow(img[0].astype('uint8'))
np.shape(img)

from google.colab import files
files.upload()

train_data = data
train_label = labels
test_data = bat_test[b'data']
test_label = bat_test[b'labels']
test_size = 10
type(data[0,0])

from knn import NearestNeighbor
NN_classifier = NearestNeighbor(k=3)
NN_classifier.train(train_data,train_label)
test_in = test_data[0:test_size]
pred = NN_classifier.predict(test_in)

print(pred)
pred_l1, pred_l2 = pred
print(pred_l1)
print(pred_l2)

num_correct = np.sum(pred_l1 == test_label[0:test_size])
accuracy_l1 = float(num_correct) / test_size
print(pred_l1)
print(test_label[0:test_size])

num_correct = np.sum(pred_l2 == test_label[0:test_size])
accuracy_l2 = float(num_correct) / test_size
print(pred_l2)
print(test_label[0:test_size])

print("The l1 accuracy is (%):", accuracy_l1*100)
print("The l2 accuracy is (%):", accuracy_l2*100)

def knn_cycle(knum):

  NN_classifier = NearestNeighbor(k=knum)
  NN_classifier.train(train_data,train_label)
  test_in = test_data[0:test_size]
  pred = NN_classifier.predict(test_in)

  print(pred)
  pred_l1, pred_l2 = pred
  print(pred_l1)

  num_correct = np.sum(pred_l1 == test_label[0:test_size])
  accuracy_l1 = float(num_correct) / test_size
  print(pred_l1)
  print(test_label[0:test_size])

  num_correct = np.sum(pred_l2 == test_label[0:test_size])
  accuracy_l2 = float(num_correct) / test_size
  print(pred_l2)
  print(test_label[0:test_size])

  print("The l1 accuracy is (%):", accuracy_l1*100)
  print("The l2 accuracy is (%):", accuracy_l2*100)

  return accuracy_l1, accuracy_l2

l1_accuracy_ls = []
l2_accuracy_ls = []
k_label = []


while(True):
  n = int(input("k값을 입력하세요: "))
  if(n%2!=0):
    break
  else:
    print("홀수를 입력해주세요.")

for knum in range(1, n+1, 2):
  a,b = knn_cycle(knum)
  l1_accuracy_ls.append(a)
  l2_accuracy_ls.append(b)
  k_label.append(knum)

import matplotlib.pyplot as plt

plt.plot(k_label, l1_accuracy_ls, label = "l1", color="green")
plt.plot(k_label, l2_accuracy_ls, label = "l2", color = "hotpink")

plt.legend()

train_data = data.astype("float")
train_label = labels
test_data = bat_test[b'data'].astype("float")
test_label = bat_test[b'labels']
test_size = 10
type(data[0,0])

classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
num_classes = len(classes)
samples_per_class = 7
for y, cls in enumerate(classes):
  idxs = np.flatnonzero(labels == y)
  idxs = np.random.choice(idxs, samples_per_class, replace=False)
  for i, idx in enumerate(idxs):
    plt_idx = i * num_classes + y + 1
    plt.subplot(samples_per_class, num_classes, plt_idx)
    plt.imshow(img[idx].astype('uint8'))
    plt.axis('off')
    if i == 0:
      plt.title(cls)
plt.show()