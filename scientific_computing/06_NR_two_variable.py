import numpy as np
from sympy import symbols, lambdify, sympify, diff
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


def part_diff(expression):
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

    x_roots: list = []          # empty list for storing the root's x values
    y_roots: list = []          # empty list for storing the root's y values
    # initialize the result matrix
    result = np.zeros((2, 1))
    for i in range(max_iter):
        X_k = np.array([x_k, y_k])[:, np.newaxis]  # initial value matrix: column matrix
        F = np.array([f(x_k, y_k), g(x_k, y_k)])[:, np.newaxis]  # function matrix

        # calculate the value using numpy function 
        # J_k = np.array([
        #     [f_x(x_k, y_k), f_y(x_k, y_k)],
        #     [g_x(x_k, y_k), g_y(x_k, y_k)],
        # ])
        # J_k_inv = np.linalg.inv(J_k)

        # Calculating the inverse using formula
        # calculating D_k
        D_k = f_x(x_k, y_k) * g_y(x_k, y_k) - g_x(x_k, y_k) * f_y(x_k, y_k)

        # calculating the jacobian inverse
        J_k_inv = (1 / D_k) * np.array([
            [g_y(x_k, y_k), -f_y(x_k, y_k)],
            [-g_x(x_k, y_k), f_x(x_k, y_k)]
        ])

        # setting the next root
        X_k_next = X_k - np.dot(J_k_inv, F)

        # appending the value of roots in the corresponding lists to use them outside the function
        # to say, plot them
        
        x_roots.append(x_k)
        y_roots.append(y_k)
        
        # updating the values of x_k and y_k for the next iteration
        x_k, y_k = X_k_next[0, 0], X_k_next[1, 0]

        result = X_k_next

    return result, x_roots, y_roots


if __name__ == '__main__':
    func_1 = "x**2 + x*y + y*y - 7"
    func_2 = "x**3 + y**3 - 9"
    initial_1, initial_2 = 1.5, 0.5
    max_iteration: int = 3

    # result: returns root and list of root's x and y values
    r = newton_raphson_two(func_1, func_2, initial_1, initial_2, max_iteration)

    root = r[0]

    print(f"Approximate value of x: {round(root[0, 0], 4)}")            # first row, first column: x value
    print(f"Approximate value of y: {round(root[1, 0], 4)}")            # second row, first column: y value


    plt.figure(figsize=(12, 8))
    plt.plot(r[1], r[2])
    plt.scatter(r[1], r[2], c='red')
    plt.title('Newton-Raphson Method for multivariable')
    plt.show()
