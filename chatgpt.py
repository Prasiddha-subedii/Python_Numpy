import numpy as np


scores = np.array([
    [78, 85, 92, 88, 76],
    [95, 91, 89, 94, 96],
    [62, 70, 68, 75, 71],
    [88, 84, 91, 90, 87],
    [73, 79, 85, 81, 77]
])

print(np.mean(scores))
print(np.mean(scores,axis=1))
print(scores[scores>np.mean(scores, axis=1)])