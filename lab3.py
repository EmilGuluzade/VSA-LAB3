def bas_diagonal_toplam(matris):
    n = len(matris)
    toplam = 0

    for i in range(n):
        toplam += matris[i][i]

    return toplam

# Örnek bir matris oluşturalım:
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Baş diagonaldeki elemanların toplamını hesaplayalım:
sonuc = bas_diagonal_toplam(matris)
print("Baş diagonaldaki elementlerin toplamı:", sonuc)
