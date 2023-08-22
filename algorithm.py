import numpy as np

# CEM
def CEM(IMG):
  x,y,z = IMG.shape
  D = IMG[60,150,:].reshape(z,1)
  TD = np.transpose(D)
  IMG1 = IMG.reshape(x*y,z)
  R = np.dot(np.transpose(IMG1),IMG1)/(x*y)
  IR = np.linalg.inv(R)
  X = (np.dot(IMG1,np.dot(IR,D)))/(np.dot(TD,np.dot(IR,D)))
  result = X.reshape(x,y)
  print(X.shape)
  return result