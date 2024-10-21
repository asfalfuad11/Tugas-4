# Mendefinisikan matriks A dan B
A = [
    [-2, 2, 3],
    [4, -6, 7],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, -8, 4],
    [3, 2, 1]
]

# Inisialisasi matriks hasil C
C = [[0, 0, 0], 
     [0, 0, 0], 
     [0, 0, 0]]

# Melakukan perkalian matriks
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Menampilkan hasil
print("Matriks A:")
for row in A:
    print(row)

print("Matriks B:")
for row in B:
    print(row)

print("Matriks Hasil C:")
for row in C:
    print(row)
