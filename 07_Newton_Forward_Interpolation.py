import numpy as np

x_values = list(range(15, 41, 5))
y_values = [np.sin((np.pi / 180) * i) for i in x_values]

table = []
for _ in range(len(y_values) - 1):
    var = [(y_values[i + 1] - y_values[i]) for i in range(len(y_values) - 1)]
    table.append(var)
    y_values = var

# table = [[(y_values[i + 1] - y_values[i]) for i in range(len(y_values) - 1)] for _ in range(len(y_values) - 1)]

[print(i) for i in table]