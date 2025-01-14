import numpy as np


m = 8
chessBoard = np.zeros((m,m))
possiblemoves = [[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
#possiblemoves =[[3,1],[-3,1],[3,-1],[-3,-1],[1,3],[1,-3],[-1,3],[-1,-3]]
trasnmatrix = np.zeros((m**2,m**2))
#print(trasnmatrix)
for i in range(m):
    for j in range(m):
        movecount = 0;
        for x in range(8):
            newpostion = [i+possiblemoves[x][0],j+possiblemoves[x][1]]
            if(newpostion[0] >= 0 and newpostion[1] >=0 and newpostion[0] <=m-1 and newpostion[1] <= m-1):
             movecount+= 1
             trasnmatrix[i*m + j][newpostion[0]*m + newpostion[1]] += 1
        chessBoard[i][j]=movecount
i=0
j=0

for i in range(m):
    for j in range(m):
        for l in range(m**2):
                trasnmatrix[m*i+j][l] *= 1/(chessBoard[i][j])
trasnmatrix[trasnmatrix == np.inf] = 0

transition_matrix_transp = trasnmatrix.T
eigenvals, eigenvects = np.linalg.eig(transition_matrix_transp)
'''
Find the indexes of the eigenvalues that are close to one.
Use them to select the target eigen vectors. Flatten the result.
'''
close_to_1_idx = np.isclose(eigenvals,1)
target_eigenvect = eigenvects[:,close_to_1_idx]
target_eigenvect = target_eigenvect[:,0]
# Turn the eigenvector elements into probabilites
stationary_distrib = target_eigenvect / sum(target_eigenvect)

print((1/stationary_distrib[0]).real)

