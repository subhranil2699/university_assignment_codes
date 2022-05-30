"""
Newton Raphson Method in Python
"""
from typing import Any
from sympy import Symbol, diff, lambdify, sympify


def derivative(expression: str) -> tuple[Any, Any]:
    """
    Calculate the derivative expression from an expression
    given by user and returns both of them
    """
    x = Symbol('x')  # creating symbol of x
    f = lambdify(x, (func_ := sympify(expression)))  # python function from expression
    f_prime = lambdify(x, (func_p_ := diff(expression)))  # derivative expression

    print(f"The function is: {func_}")
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
    for i in range(max_iter + 1):
        # Newton Raphson method to calculate the root
        new_root = appx_root - (h := f(appx_root) / f_prime(appx_root))

        if abs(h) <= err:  # if the value of h is less than the max error
            root = new_root  # returns the calculated root
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            break  # break the infinite loop here
        else:
            print(f"{i}\t|{appx_root:0.5f}\t|{f(appx_root):0.5f}\t|{new_root:0.5f}\t|{h:0.5f}\t|")
            appx_root = new_root  # previous root becomes the new root

    # returns root if it has been found in the max error range / returns None
    return root if root else "\nInsufficient Iteration!!!"


if __name__ == '__main__':
    func: str = "x**3 - 2*x - 5"
    result: Any = newton_raphson(func, 2.0, 0.00001, 3)
    print(result)
