def tower_hanoi(n, a, b, c):
    if n == 0:
        return
    if n == 1:
        print(a, c)
        return
    tower_hanoi(n - 1, a, c, b)
    print(a, c)
    tower_hanoi(n - 1, b, a, c)
n = int(input())
tower_hanoi(n, "a", "b", "c")
