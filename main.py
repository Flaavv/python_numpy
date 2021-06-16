import numpy as np


rdm_mat = np.random.rand(5, 4)
print(rdm_mat)


print(type(rdm_mat))


print(rdm_mat.sum())


print(np.max(rdm_mat, 1))


print(np.max(rdm_mat, 0))


print([x.max() for x in rdm_mat])


rdm_vec = np.random.random(100)
print(rdm_vec)


print(rdm_vec.argmax())


print(rdm_vec.max())


rdm_vec = rdm_vec.reshape([10, 10])
print(rdm_vec)


print(rdm_vec.mean(1))


print(rdm_vec.mean(0))


print(rdm_vec.sum(0))


print(rdm_vec.sum(1))