"""
Subhranil Sarkar
Bisection code
"""

from typing import Callable, Any
import numpy as np


# bisection function
def bisection(func: Callable[[float], float],
              a: float,
              b: float,
              e: float = 0.001,
              table: bool = False) -> Any:
    '''
    bisection method to calculate root between two values
    '''
    if func(a) * func(b) >= 0:                                                                              # intermediate theorem invalid here
        print(f"There is no root in between {a} and {b}")
        return None

    else:
        s = "a\t|b\t\t|f(a)\t\t|f(b)\t\t|root\t\t|f(root)\t|\n"
        while abs(b - a) >= e:
            if func((root := (a + b) / 2.0)) == 0:                                                          # exact root
                return root
            elif (f_r := func(root)) * (f_a := func(a)) < 0:                                                # root lies in between (a, root)
                s += f"{a:0.5f}\t|{b:0.5f}\t|{f_a:0.5f}\t|{func(b):0.5f}\t|{root:0.5f}\t|{f_r:0.5f}\t|\n"
                b = root
            else:                                                                                           # root lies in between (root, b)
                s += f"{a:0.5f}\t|{b:0.5f}\t|{f_a:0.5f}\t|{func(b):0.5f}\t|{root:0.5f}\t|{f_r:0.5f}\t|\n"
                a = root

        # return table 
        if table:
          return {"root": root, "table": s}
        
        # return root only
        return root


if __name__ == "__main__":
    root = bisection(lambda x: np.power(x, 3) - 5 * x - 2, 2.0, 3.0, 0.0001, True)
    print("The root is = ", root["root"])
    print()
    print(root["table"])
