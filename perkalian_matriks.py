def multiply_matrices(A, B):
    # Inisialisasi matriks hasil C dengan 0
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # Perkalian matriks
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Input matriks A 3x3
A = []
print("Masukkan elemen matriks A (3x3):")
for i in range(3):
    row = list(map(int, input(f"Baris {i + 1} (pisahkan dengan spasi): ").split()))
    if len(row) != 3:
        print("Matriks A harus berordo 3x3.")
        exit()
    A.append(row)

# Input matriks B 3x3
B = []
print("Masukkan elemen matriks B (3x3):")
for i in range(3):
    row = list(map(int, input(f"Baris {i + 1} (pisahkan dengan spasi): ").split()))
    if len(row) != 3:
        print("Matriks B harus berordo 3x3.")
        exit()
    B.append(row)

# Melakukan perkalian matriks
C = multiply_matrices(A, B)

# Menampilkan hasil
print("Hasil Perkalian Matriks C:")
for row in C:
    print(row)
