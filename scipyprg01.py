from scipy import sparse
def get_coo_matrix(values):
    data, row, col = [],[],[]
    for i,value in enumerate(values):
        n = len(value)
        data.extend(value)
        row.extend([i]*n)
        col.extend(list(range(n)))
    return sparse.coo_matrix((data,(row,col)))
values = [[1],[1,2],[1,2,3],[4,5,6,7],[8,9,10,11,12]]
M = get_coo_matrix(values)
print(M)
