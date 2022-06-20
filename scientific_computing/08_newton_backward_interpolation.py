import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn-whitegrid')



def factorial(x):
    assert x >= 0, "Sorry -ve number is not allowed"
    r = 1
    for i in range(x, 0, -1):
        r *= i
    return r


x = np.arange(0.1, 0.6, 0.1)
y = np.exp(2 * x)
h = x[1] - x[0]



def get_table(y):
    n = len(y)
    coef = np.zeros((n, n))
    coef[:, 0] = y

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            coef[j][i] = coef[j][i-1] - coef[j-1][i-1]
    
    return coef

tabl = get_table(y)


def newton_backward(x_value, table, x, y):
    result = y[-1]
    n = len(x)
    for i in range(1, len(x)):
        rk = 1
        an = table[len(x) - 1][i] / (factorial(i) * np.power(h, (i)))
        # print(an)
        for j in range(n-1, n-i-1, -1):
            rk *= x_value - x[j]
        result += rk * an

    return result



x_val = 0.37
result = newton_backward(x_val, tabl, x, y)

print(f"Value of f({x_val}) = {result:0.6f}")


# plotting

x_new = np.linspace(-1, 2.1, 1000)
y_new = newton_backward(x_new, tabl, x, y)

plt.figure(figsize = (12, 8))
plt.plot(x_new, y_new, label="Estimatd function")
plt.plot(x_new, np.exp(2*x_new), '--r',label="Actual function")
plt.plot(x, y, 'ko', label="Given Points")
plt.title("Newton Backward Interpolation")

plt.legend()
plt.savefig('Newton_backward_interpolation.jpg')
plt.show()
