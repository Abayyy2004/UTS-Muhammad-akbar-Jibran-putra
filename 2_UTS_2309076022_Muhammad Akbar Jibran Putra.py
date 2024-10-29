import numpy as np

# a) Fungsi untuk menyelesaikan sistem persamaan linear menggunakan metode eliminasi Gauss
def gaussian_elimination(A, b):
    n = len(b)
    # Gabungkan A dan b
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Eliminasi ke atas
    for i in range(n):
        # Normalisasi baris
        Ab[i] = Ab[i] / Ab[i, i]
        
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[i] * Ab[j, i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i+1:n] * x[i+1:n])
    
    return x

# b) Fungsi untuk menghitung determinan matriks menggunakan ekspansi kofaktor
def determinant(A):
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    elif n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    else:
        det = 0
        for c in range(n):
            det += ((-1) ** c) * A[0, c] * determinant(A[1:, np.arange(n) != c])
        return det

# c) Menggunakan kedua fungsi untuk menyelesaikan sistem persamaan di atas
# Persamaan dalam bentuk matriks Ax = b
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [1, -1, 5]], dtype=float)

b = np.array([5, 3, 4], dtype=float)

# Menyelesaikan sistem persamaan menggunakan eliminasi Gauss
solution_gauss = gaussian_elimination(A, b)
print("Solusi menggunakan Metode Eliminasi Gauss:", solution_gauss)

# Menghitung determinan matriks
det_A = determinant(A)
print("Determinant dari matriks A:", det_A)

# d) Implementasikan metode Gauss-Jordan
def gauss_jordan(A, b):
    n = len(b)
    # Gabungkan A dan b
    Ab = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        # Normalisasi baris
        Ab[i] = Ab[i] / Ab[i, i]
        
        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[i] * Ab[j, i]

    return Ab[:, -1]  # Solusi di kolom terakhir

# Menyelesaikan dengan metode Gauss-Jordan
solution_gauss_jordan = gauss_jordan(A, b)
print("Solusi menggunakan Metode Gauss-Jordan:", solution_gauss_jordan)

# e) Fungsi untuk menghitung invers matriks menggunakan metode adjoin
def inverse_matrix(A):
    det = determinant(A)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers (determinant = 0)")
    n = A.shape[0]
    adjoint = np.zeros(A.shape)
    for i in range(n):
        for j in range(n):
            # Membentuk matriks minor
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            adjoint[j, i] = ((-1) ** (i + j)) * determinant(minor)  # Transpose dan tanda
    return adjoint / det  # Menghitung invers

# Menghitung invers matriks A
try:
    inverse_A = inverse_matrix(A)
    print("Invers dari matriks A:")
    print(inverse_A)
except ValueError as e:
    print(e)