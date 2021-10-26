import random

#declare range of password from 0 to 9
password = range(10)

#Randomize the password
x1 =  str(random.choice(password))

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



    
