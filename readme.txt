




FUNCTION multiply_matrices(A, B)
    INITIALIZE C as 3x3 matrix with all elements = 0

    FOR i FROM 0 TO 2 DO
        FOR j FROM 0 TO 2 DO
            FOR k FROM 0 TO 2 DO
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
            END FOR
        END FOR
    END FOR

    RETURN C
END FUNCTION

START
    INITIALIZE A as empty list
    PRINT "Masukkan elemen matriks A (3x3):"
    FOR i FROM 0 TO 2 DO
        INPUT row
        IF length(row) != 3 THEN
            PRINT "Matriks A harus berordo 3x3."
            EXIT
        END IF
        APPEND row to A
    END FOR

    INITIALIZE B as empty list
    PRINT "Masukkan elemen matriks B (3x3):"
    FOR i FROM 0 TO 2 DO
        INPUT row
        IF length(row) != 3 THEN
            PRINT "Matriks B harus berordo 3x3."
            EXIT
        END IF
        APPEND row to B
    END FOR

    C = multiply_matrices(A, B)

    PRINT "Hasil Perkalian Matriks C:"
    FOR each row in C DO
        PRINT row
    END FOR
END
