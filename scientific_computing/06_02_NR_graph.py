import numpy as np
from sympy import symbols, lambdify, sympify, diff
import matplotlib.pyplot as plt


def part_diff(expression: str):
    x, y = symbols('x y')
    f = lambdify([x, y], (f_ := sympify(expression)))
    f_x = lambdify([x, y], (f_x_ := diff(expression, x)))
    f_y = lambdify([x, y], (f_y_ := diff(expression, y)))

    print(f"The function is: {f_}")
    print(f"Partial diff w.r.t. x is: {f_x_}")
    print(f"Partial diff w.r.t. y is: {f_y_}\n")

    return f, f_x, f_y


def newton_raphson_two(func_1, func_2, x_k, y_k, max_iter):
    f, f_x, f_y = part_diff(func_1)
    g, g_x, g_y = part_diff(func_2)

    x_roots = []
    y_roots = []
    result = np.zeros((2, 1))
    for i in range(max_iter):
        X_k = np.array([x_k, y_k])[:, np.newaxis]  # initial value matrix
        F = np.array([f(x_k, y_k), g(x_k, y_k)])[:, np.newaxis]  # function matrix

        # J_k = np.array([
        #     [f_x(x_k, y_k), f_y(x_k, y_k)],
        #     [g_x(x_k, y_k), g_y(x_k, y_k)],
        # ])
        # J_k_inv = np.linalg.inv(J_k)

        # calculating D_k
        D_k = f_x(x_k, y_k) * g_y(x_k, y_k) - g_x(x_k, y_k) * f_y(x_k, y_k)

        # calculating the jacobian inverse
        J_k_inv = (1 / D_k) * np.array([
            [g_y(x_k, y_k), -f_y(x_k, y_k)],
            [-g_x(x_k, y_k), f_x(x_k, y_k)]
        ])

        # setting the next root
        X_k_1 = X_k - np.dot(J_k_inv, F)

        # updating the values of x_k and y_k
        x_roots.append(x_k)
        y_roots.append(y_k)
        x_k, y_k = X_k_1[0, 0], X_k_1[1, 0]

        result = X_k_1

    return result, x_roots, y_roots


if __name__ == '__main__':
    func_1: str = "x**2 + x*y + y*y - 7"
    func_2: str = "x**3 + y**3 - 9"

    initial_1, initial_2 = 1.5, 0.5

    max_iteration: int = 3

    r = newton_raphson_two(func_1, func_2, initial_1, initial_2, max_iteration)

    print(f"Approximate value of x: {round(r[0][0, 0], 4)}")
    print(f"Approximate value of y: {round(r[0][1, 0], 4)}")

    f_1 = lambda x, y: x ** 2 + x * y + y * y - 7
    f_2 = lambda x, y: x ** 3 + y ** 3 - 9

    x_roots = r[1]
    y_roots = r[2]

    print(r[1])
    print(r[2])

    plt.plot(x_roots, y_roots)
    plt.show()
