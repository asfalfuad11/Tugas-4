PSEUDOCODE
BEGIN
    // Definisikan matriks A dan B
    DECLARE A[3][3] = [ [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9] ]

    DECLARE B[3][3] = [ [9, 8, 7],
                        [6, 5, 4],
                        [3, 2, 1] ]

    // Cek apakah matriks dapat dikalikan
    IF (kolom A != baris B) THEN
        PRINT "Perkalian tidak dapat dilakukan!"
    ELSE
        // Inisialisasi matriks hasil C
        DECLARE C[3][3]
        FOR i FROM 0 TO 2 DO
            FOR j FROM 0 TO 2 DO
                C[i][j] = 0
            END FOR
        END FOR

        // Melakukan perkalian
        FOR i FROM 0 TO 2 DO
            FOR j FROM 0 TO 2 DO
                FOR k FROM 0 TO 2 DO
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
                END FOR
            END FOR
        END FOR

        // Menampilkan hasil
        PRINT "Matriks Hasil C:"
        FOR i FROM 0 TO 2 DO
            PRINT C[i]
        END FOR
    END IF
END
