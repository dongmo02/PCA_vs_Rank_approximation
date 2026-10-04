import numpy as np
import scipy
import numpy.linalg
import matplotlib.pyplot as plt
from numpy.ma.core import reshape, around
from sklearn.datasets import fetch_openml
plt.style.use('fivethirtyeight')
mnist = fetch_openml('mnist_784', version=1, as_frame=False)

Images = mnist.data
y = mnist.target
# Take 6000 images
Images = Images[:6000]
'''plt.figure(figsize=(4,4))
plt.grid(False)
plt.axis("off")
plt.imshow(Images[0].reshape((28,28))  , cmap='gray')
plt.show() '''


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def normalize(X):
    """Normalize the given dataset X to have zero mean.
    Args:
        X: ndarray, dataset of shape (N,D) where D is the dimension of the data,
           and N is the number of datapoints

    Returns:
        (Xbar, mean): tuple of ndarray, Xbar is the normalized dataset
        with mean 0; mean is the sample mean of the dataset.
    """
    N, D = X.shape
    mu = 0
    i = 0
    v = 0
    print(f"  v: {v}")
    while i < N:
        v += X[i]
        i += 1
    mu = v / N
    print(mu)
    Xbar = (X - mu)
    print(np.sum(Xbar))
    return Xbar, mu


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def eig(S):
    """Compute the eigenvalues and corresponding eigenvectors
        for the covariance matrix S.
    Args:
        S: ndarray, covariance matrix

    Returns:
        (eigvals, eigvecs): ndarray, the eigenvalues and eigenvectors

    Note:
        the eigenvals and eigenvecs should be sorted in descending
        order of the eigen values
    """
    eigvals, eigvecs = np.linalg.eigh(S)
    sort_indices = eigvals.argsort()[::-1]
    return eigvals[sort_indices], eigvecs[:, sort_indices]


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def projection_matrix(B):
    """Compute the projection matrix onto the space spanned by `B`
    Args:
        B: ndarray of dimension (D, M), the basis for the subspace

    Returns:
        P: the projection matrix
    """
    P = B @ np.linalg.inv(  B.transpose() @ B) @ B.transpose()
    return P


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def PCA(X, num_components):
    """
    Args:
        X: ndarray of size (N, D), where D is the dimension of the data,
           and N is the number of datapoints
        num_components: the number of principal components to use.
    Returns:
        the reconstructed data, the sample mean of the X, principal values
        and principal components
    """
    X_normalized = X # EDIT THIS
    S =  (X_normalized.transpose()  @ X_normalized) / X.shape[0] # EDIT THIS
    eig_vals, eig_vecs = eig(S) # EDIT THIS
    principal_vals, principal_components = eig_vals[0:num_components], eig_vecs[:,0:num_components]
    B = np.array(principal_components)
    print(principal_components.shape , eig_vecs.shape)
    P = projection_matrix(B)
    reconst = np.zeros_like(X_normalized)
    reconst = (P @ X_normalized.T).T
    return reconst,  principal_vals, principal_components

def RanK_appro(X , num_components):
    num_components = np.around(np.sqrt(num_components))
    X = X.reshape((28,28))
    U , sigma , V = np.linalg.svd(X)
    num_components = int(num_components)
    appro_X = U[:,:num_components] @ np.diag(sigma[:num_components])  @ V[:num_components]
    return appro_X

reconst,  principal_vals, principal_components = PCA(Images , 392)
print(principal_components)
plt.figure(figsize=(8,8))
# Original Image and Image compress with PCA
plt.subplot(2,2,1)
plt.imshow( Images[0].reshape((28,28)) , cmap="gray")
plt.grid(False)
plt.axis("off")
#Compress Image with PCA
plt.subplot(2,2,2)
plt.imshow( reconst[0].reshape((28,28)) , cmap="gray")
plt.grid(False)
plt.axis("off")
# Original Image and Image compress with Rank-approximation
plt.subplot(2,2,3)
plt.imshow( Images[0].reshape((28,28)) , cmap="gray")
plt.grid(False)
plt.axis("off")
# Compress Image with rank-approximation
plt.subplot(2,2,4)
plt.imshow( RanK_appro(Images[0] , 196) , cmap="gray")
plt.grid(False)
plt.axis("off")


plt.show()

