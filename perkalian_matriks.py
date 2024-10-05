# Masukkan angka untuk matriks A dan B
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def multiply_matrices(A, B):
    # Inisialisasi matriks hasil C
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Melakukan perkalian matriks
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Cek apakah matriks dapat dikalikan
if len(A[0]) != len(B):
    print("Perkalian matriks tidak dapat dilakukan!")
else:
    C = multiply_matrices(A, B)
    print("Matriks Hasil C:")
    for row in C:
        print(row)
