
n = 5
y = [4, 6, 6, 4, 4, 5]
x_last = 10
x_first = 0
interval = len([*range(x_first,x_last)])/n
print(interval)

def trapezoidal_rule(y):
    result = 0
    result = sum([(result + (2 * i)) for i in y[1:-1]])
    answer = (result + y[0] + y[len(y)-1]) * interval/2
    print(answer)

trapezoidal_rule(y)