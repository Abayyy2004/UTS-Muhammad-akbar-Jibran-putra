import numpy as np

# a) Fungsi resistansi termistor
def R(T):
    return 5000 * (1 - (3500 / (T + 298)))

# a) Fungsi untuk menghitung selisih maju, mundur, dan tengah
def forward_difference(func, T, dT):
    return (func(T + dT) - func(T)) / dT

def backward_difference(func, T, dT):
    return (func(T) - func(T - dT)) / dT

def central_difference(func, T, dT):
    return (func(T + dT) - func(T - dT)) / (2 * dT)

# b) Fungsi untuk menghitung nilai eksak
def exact_derivative(T):
    return (5000 * 3500) / ((T + 298) ** 2)

# c) Hitung pada rentang temperatur 250K sampai 350K dengan interval 10K
T_values = np.arange(250, 360, 10)
dT = 10  # interval temperatur

# Menyimpan hasil perhitungan
results = {
    "T": T_values,
    "Forward": [forward_difference(R, T, dT) for T in T_values],
    "Backward": [backward_difference(R, T, dT) for T in T_values],
    "Central": [central_difference(R, T, dT) for T in T_values],
    "Exact": [exact_derivative(T) for T in T_values],
}

# d) Hitung dan cetak error relatif
errors = {
    "Forward": np.abs((np.array(results["Forward"]) - np.array(results["Exact"])) / results["Exact"]),
    "Backward": np.abs((np.array(results["Backward"]) - np.array(results["Exact"])) / results["Exact"]),
    "Central": np.abs((np.array(results["Central"]) - np.array(results["Exact"])) / results["Exact"]),
}

# Tampilkan hasil
print("Temperatur (K) | Forward | Backward | Central | Exact | Error Forward | Error Backward | Error Central")
for i in range(len(T_values)):
    print(f"{T_values[i]:<15} | {results['Forward'][i]:<7.4f} | {results['Backward'][i]:<8.4f} | {results['Central'][i]:<7.4f} | {results['Exact'][i]:<5.4f} | "
          f"{errors['Forward'][i]:<10.4f} | {errors['Backward'][i]:<10.4f} | {errors['Central'][i]:<10.4f}")

# e) Metode Extrapolasi Richardson
def richardson_extrapolation(f, T, dT):
    forward = forward_difference(f, T, dT)
    backward = backward_difference(f, T, dT)
    return (4 * forward - backward) / 3  # Richardson's formula for accuracy improvement

# Hitung hasil dengan extrapolasi Richardson
richardson_results = {
    "T": T_values,
    "Richardson": [richardson_extrapolation(R, T, dT) for T in T_values],
}

# Hitung error relatif untuk Richardson
richardson_errors = np.abs((np.array(richardson_results["Richardson"]) - np.array(results["Exact"])) / results["Exact"])

# Tampilkan hasil Richardson
print("\nTemperatur (K) | Richardson | Error Richardson")
for i in range(len(T_values)):
    print(f"{T_values[i]:<15} | {richardson_results['Richardson'][i]:<10.4f} | {richardson_errors[i]:<15.4f}")

# Bandingkan hasilnya
print("\nPerbandingan hasil akhir:")
for i in range(len(T_values)):
    print(f"T = {T_values[i]} K: Exact = {results['Exact'][i]:.4f}, Richardson = {richardson_results['Richardson'][i]:.4f}, "
          f"Error = {richardson_errors[i]:.4f}")