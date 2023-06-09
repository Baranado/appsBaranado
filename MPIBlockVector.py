from pyomo.contrib.pynumero.sparse.mpi_block_vector import MPIBlockVector
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
owners = [2, 0, 1]
x = MPIBlockVector(3, rank_owner=owners, mpi_comm=comm)
x.set_block(owners.index(rank), np.random.normal(size=3))
y = MPIBlockVector(3, rank_owner=owners, mpi_comm=comm)
y.set_block(owners.index(rank), np.random.normal(size=3))
z1 = x + y # add x and y
z2 = x.dot(y) # dot product
z3 = x.max() # infinity norm
print(f"z1\n{z1}")
print(f"z2\n{z2}")
print(f"z3\n{z3}")
