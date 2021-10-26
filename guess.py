import random

password = range(10)

x1 =  str(random.choice(password))
print(x1)
count = 1

while True: 
    answer = input("masukkan salah satu angka dari 0 sampai dengan 9 = ")
    print('Percobaan ke-', count)
    if x1 == answer:
        print('Selamat anda berhasil')
        break
    else:
        print('Maaf anda gagal!')
        count = count + 1
        True
        if count > 3:
            print('Game Over')
            exit()


    