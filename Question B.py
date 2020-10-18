from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
number_of_processors = comm.Get_size()

if rank != 0:
    message = "You rock, you are number :" + str(rank)
    comm.send(message, dest=0)
    print("Hello from:" + str(rank))
else:
    for procid in range(1, number_of_processors):
        message = comm.recv(source=procid)
        print("Process O receives messages from", procid, ":", message)
