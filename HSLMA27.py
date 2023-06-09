
from scipy.sparse import tril 
from pyomo.contrib.pynumero.linalg.ma27 import MA27Interface
A = get_coo_matrix()
rhs = get_rhs()
solver = MA27Interface()
solver.set_cntl(1, 1e-6)
# set the pivot tolerance
A_tril = tril(A)
# extract lower triangular portion of A
status = solver.do_symbolic_factorization(dim=5, irn=A_tril.row, icn=A_tril.col)
status = solver.do_numeric_factorization(dim=5, irn=A_tril.row, icn=A_tril.col, entries=A_tril.data)
x = solver.do_backsolve(rhs)
