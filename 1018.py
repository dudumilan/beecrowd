N = int(input())
print(N)
for nota in [100, 50, 20, 10, 5, 2, 1]:
    qnt = N // nota
    print(f"{qnt} nota(s) de R$ {nota},00")
    N %= nota
