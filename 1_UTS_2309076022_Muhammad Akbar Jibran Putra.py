import numpy as np

# Parameter
L = 0.5  # Henry
C = 10e-6  # Farad
target_frequency = 1000  # Hz
tolerance = 0.1

# a) Fungsi untuk menghitung f(R) dan f'(R)
def f(R):
    # Menjaga agar argumen dalam akar kuadrat tetap non-negatif
    discriminant = 1 / (L * C) - (R * 2) / (4 * L * 2)
    if discriminant < 0:
        return float('nan')  # Mengembalikan NaN jika argumen akar negatif
    return (1 / (2 * np.pi)) * np.sqrt(discriminant)

def f_prime(R):
    discriminant = 1 / (L * C) - (R * 2) / (4 * L * 2)
    if discriminant <= 0:
        return float('nan')  # Mengembalikan NaN jika argumen akar negatif
    return (-R / (4 * np.pi * L)) * (1 / np.sqrt(discriminant))

# Fungsi yang akan dicari akarnya: f(R) - target_frequency
def g(R):
    return f(R) - target_frequency

# b) Metode Biseksi
def bisection_method(a, b, tol):
    iterations = []
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        iterations.append(midpoint)
        if np.isnan(g(midpoint)):
            return midpoint, iterations  # Menghindari NaN
        if g(midpoint) == 0 or (b - a) / 2 < tol:
            return midpoint, iterations
        elif g(a) * g(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2, iterations

# c) Metode Newton-Raphson
def newton_raphson_method(initial_guess, tol):
    R = initial_guess
    iterations = [R]
    while abs(g(R)) > tol:
        if np.isnan(f_prime(R)):  # Cek jika f'(R) tidak valid
            return float('nan'), iterations  # Mengembalikan NaN jika tidak valid
        R -= g(R) / f_prime(R)
        iterations.append(R)
    return R, iterations

# Menjalankan metode bisection
R_bisection, bisection_iterations = bisection_method(0, 100, tolerance)

# Menjalankan metode Newton-Raphson
R_newton, newton_iterations = newton_raphson_method(50, tolerance)

# Menampilkan hasil
print("Hasil Metode Biseksi: R =", R_bisection)
print("Iterasi Biseksi:", len(bisection_iterations))

print("Hasil Metode Newton-Raphson: R =", R_newton)
print("Iterasi Newton-Raphson:", len(newton_iterations))

# Membandingkan hasil
print("\nPerbandingan Hasil:")
print(f"R (Biseksi): {R_bisection:.4f} Ohm")
print(f"R (Newton-Raphson): {R_newton:.4f} Ohm")