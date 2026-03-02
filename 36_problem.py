'''labels = np.array([0, 2, 1, 2, 0])
Convert this into one-hot encoded format using NumPy only.
Expected shape:
(5, 3)
This is directly used in classification models.'''
import numpy as np
labels=np.array([0,  2, 1, 2, 0])
num_classes=np.max(labels) + 1
one_hot_expected=np.eye(num_classes)[labels]
print(one_hot_expected)
print("Shape:",one_hot_expected.shape)