
from pyomo.contrib.pynumero.sparse import BlockVector
import numpy as np
x = BlockVector(2)
x.set_block(0, np.random.normal(size=3))
x.set_block(1, np.random.normal(size=3))
y = BlockVector(2)
y.set_block(0, np.random.normal(size=3))
y.set_block(1, np.random.normal(size=3))
# add x and y
z = x + y
print(f"x:\n{x}")
print(f"y:\n{y}")
print(f"z:\n{z}")
