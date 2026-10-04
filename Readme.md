# PCA vs Rank Approximation

This project compares **PCA** and **rank approximation** for image compression.

Both methods are used to reduce the dimensionality of MNIST images and reconstruct them using fewer components.

## Goal

Compare the reconstruction quality of PCA and rank approximation for different numbers of components.

## Methods

- **PCA:** reduces the 784-dimensional image representation using principal components.
- **Rank approximation:** uses SVD to approximate each 28×28 image with a lower-rank matrix.

The reconstructed images are compared visually and using reconstruction error.

## Tools

- Python
- NumPy
- Matplotlib
- MNIST dataset