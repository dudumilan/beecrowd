meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

numero = int(input())

if 1 <= numero <= 12:
    print(meses[numero - 1])
