"""
Method of False Position
also known as Regula-falsi
"""
from typing import Callable


def regula_falsi(func: Callable[[float], float], point_1: float, point_2: float, err: float) -> float:
    """
    Regula falsi method
    """
    if func(point_1) * func(point_2) >= 0:
        print(f"There's no root in between {point_1} and {point_2}")
        return None
    else:
        n: int = 0
        print("n\t|a\t\t\t|b\t\t\t|f(a)\t\t|f(b)\t\t|root\t\t|f(root)\t|")
        while abs(f_r := (func(root := (point_1 * (f_point_2 := func(point_2)) - point_2 * (f_point_1 := func(point_1))) / (f_point_2 - f_point_1)))) >= err:
            if f_r * f_point_1 < 0:
                print(f"{n}\t|{point_1:0.5f}\t|{point_2:0.5f}\t|{f_point_1:0.5f}\t|{root:0.5f}\t|{f_r:0.5f}\t|")
                point_2 = root
            elif f_r * f_point_2 < 0:
                print(f"{n}\t|{point_1:0.5f}\t|{point_2:0.5f}\t|{f_point_1:0.5f}\t|{f_point_2:0.5f}\t|{root:0.5f}\t|{f_r:0.5f}\t|")
                point_1 = root
            n += 1

        return root


if __name__ == '__main__':
    func: Callable[[float], float] = lambda x: x ** 3 - 2 * x - 5
    print(regula_falsi(func, 2.0, 3.0, 0.001))
