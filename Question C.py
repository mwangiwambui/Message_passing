from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
number_of_processors = comm.Get_size()
n = 5
y = [4, 6, 6, 4, 4, 5]
x_last = 10
x_first = 0
interval = len([*range(x_first, x_last)]) / n
y1 = [4, 6, 6]
y2 = [6, 4, 4]
y3 = [4, 5]
total_area = 0

def trapezoidal_rule(y):
    result = 0
    result = sum([(result + (2 * i)) for i in y[1:-1]])
    answer = (result + y[0] + y[len(y) - 1]) * interval / 2
    return answer

if rank != 0:
    if rank == 1:
        message = trapezoidal_rule(y1)
        comm.send(message, dest=0)
    elif rank == 2:
        message = trapezoidal_rule(y2)
        comm.send(message, dest=0)
    elif rank == 3:
        message = trapezoidal_rule(y3)
        comm.send(message, dest=0)
    print("Hello from:" + str(rank))
else:
    for procid in range(1, number_of_processors):
        message = comm.recv(source=procid)
        total_area += message
        print('Calculated area from process {} is : {}'.format(procid, message))

    if total_area > 0:
        print('Total trapezium area is : {}'.format(total_area))
        print(message)
