import numpy as np
from numpy import ndarray
from typing import Any

from sympy import symbols, lambdify, sympify, diff


def part_diff(expression: str) -> tuple[Any, ...]:
    x, y = symbols('x y')
    f: Any = lambdify([x, y], (f_ := sympify(expression)))
    f_x: Any = lambdify([x, y], (f_x_ := diff(expression, x)))
    f_y: Any = lambdify([x, y], (f_y_ := diff(expression, y)))

    print(f"The function is: {f_}")
    print(f"Partial diff w.r.t. x is: {f_x_}")
    print(f"Partial diff w.r.t. y is: {f_y_}\n")

    return f, f_x, f_y


def newton_raphson_two(func_1: str, func_2: str, x_k: float, y_k: float, max_iter: int) -> ndarray:
    f, f_x, f_y = part_diff(func_1)
    g, g_x, g_y = part_diff(func_2)

    result: ndarray = np.zeros((2, 1))
    for i in range(max_iter):
        X_k: ndarray = np.array([x_k, y_k])[:, np.newaxis]
        F: ndarray = np.array([f(x_k, y_k), g(x_k, y_k)])[:, np.newaxis]

        # J_k = np.array([
        #     [f_x(x_k, y_k), f_y(x_k, y_k)],
        #     [g_x(x_k, y_k), g_y(x_k, y_k)],
        # ])
        # J_k_inv = np.linalg.inv(J_k)

        # calculating D_k
        D_k: float = f_x(x_k, y_k) * g_y(x_k, y_k) - g_x(x_k, y_k) * f_y(x_k, y_k)

        # calculating the jacobian inverse
        J_k_inv = (1 / D_k) * np.array([
            [g_y(x_k, y_k), -f_y(x_k, y_k)],
            [-g_x(x_k, y_k), f_x(x_k, y_k)]
        ])

        # setting the next root
        X_k_1 = X_k - np.dot(J_k_inv, F)

        # updating the values of x_k and y_k
        x_k, y_k = X_k_1[0, 0], X_k_1[1, 0]

        result = X_k_1

    return result


if __name__ == '__main__':
    func_1: str = "x**2 + x*y + y*y - 7"
    func_2: str = "x**3 + y**3 - 9"

    initial_1, initial_2 = 1.5, 0.5

    max_iteration: int = 3

    r: ndarray = newton_raphson_two(func_1, func_2, initial_1, initial_2, max_iteration)

    print(f"Approximate value of x: {round(r[0, 0], 4)}")
    print(f"Approximate value of y: {round(r[1, 0], 4)}")
