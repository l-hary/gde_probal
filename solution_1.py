"""Készítsen sztring összeadó, kivonó, összehasonlító, szorzó algoritmusokat! (4 fő)
Az algoritmus paraméterként két pozitív egész számokat tartalmazó sztringet kap, melyekkel elvégzi a kívánt
műveletet. Összeadás esetén visszatér a két szám összegét tartalmazó sztringgel. Kivonás esetén a két szám
különbségét tartalmazó sztringgel. Összehasonlítás esetén a visszatérési érték legyen 1 ha az első szám a
kisebb, legyen -1 ha a második paraméterként kapott szám a kisebb és 0, ha egyenlő a két szám. Szorzás
esetén a szorzattal térjen vissza.
Valósítsa meg azokat az algoritmusokat is, amelyek a negatív számokat is kezelik!
"""


def main() -> None:
    nums = input("what's the meaning of life?: ")
    nums = [int(x) for x in nums.split()]

    addition = sum(nums)
    subtraction = nums[0] - nums[1]
    comparison = 1 if nums[0] < nums[1] else -1 if nums[0] > nums[1] else 0
    multiplication = nums[0] * nums[1]

    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Comparison: {comparison}")
    print(f"Multiplication: {multiplication}")


if __name__ == "__main__":
    main()
