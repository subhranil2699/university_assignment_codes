"""
Newton Raphson Method in Python
"""
from typing import Any
from sympy import Symbol, diff, lambdify, sympify
import matplotlib.pyplot as plt
import numpy as np


# plt.style.use('fivethirtyeight')


def derivative(expression: str) -> tuple[Any, Any]:
    """
    Calculate the derivative expression from an expression
    given by user and returns both of them
    """
    x = Symbol('x')  # creating symbol of x
    # python function from expression
    f = lambdify(x, (func_ := sympify(expression)))
    f_prime = lambdify(x, (func_p_ := diff(expression)))  # derivative expression

    print(f"The function is: {func_}")  # print the function
    # print the derivative of the function
    print(f"The derivative of the function is: {func_p_}")

    # returns the function and its derivative
    return f, f_prime


def newton_raphson(func: str, appx_root: float, err: float = 0.01, max_iter: int = 10) -> Any:
    """
    Calculates Newton-Raphson Method
    """

    f, f_prime = derivative(func)
    root = None
    print("\nn\t|x_n\t\t|f(x_n)\t\t|x_(n+1)\t|h\t\t\t|")

    roots = []
    for i in range(max_iter + 1):
        # Newton Raphson method to calculate the root
        new_root = appx_root - (h := f(appx_root) / f_prime(appx_root))

        if abs(h) <= err:  # if the value of h is less than the max error
            root = new_root  # returns the calculated root
            # fstring
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            break  # break the infinite loop here
        else:
            # fstring
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            appx_root = new_root  # previous root becomes the new root
        roots.append(new_root)

    # returns root if it has been found in the max error range / returns None

    return root if root else "\nInsufficient Iteration!!!", roots


if __name__ == '__main__':
    func: str = "cos(x)-exp(x)"

    for i in range(10):
        result: Any = newton_raphson(func, 2.0, 0.0000000001, i)
        if result[0] != "\nInsufficient Iteration!!!":
            print(f"\nThe root is: {result[0]}")
            break

    y = list(map(lambda x: np.cos(x) - np.exp(x), result[1]))
    print(y)
    plt.subplot(2, 1, 1)
    plt.plot((x := np.linspace(-10, 10, 1000)), (lambda i: np.cos(i) - np.exp(i))(x), label="f(x)")
    plt.plot(result[1])
    plt.plot(result[1], y, '.', label="x")
    plt.axhline(0, color='red', alpha=0.5)
    plt.axvline(0, color='red', alpha=0.5)
    plt.xlabel("$x$")
    plt.ylabel("$f(x) = cos(x)-e^x$")

    plt.subplot(2, 1, 2)
    plt.plot(result[1])

    # plt.xlim(2.09, 2.102)
    # plt.ylim(-0.9, 1.0)
    plt.legend()
    plt.show()
