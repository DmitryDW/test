from my_test1 import full_name

print("Для остановки нажмите 'Q'")

while True:
    first = input("\nВведите ваше имя: ")
    if first == 'Q':
        break
    last = input("\nВведите вашу фамилию: ")
    if first == 'Q':
        break

    your_name = full_name(first, last)
    print("\tВас зовут: " + your_name)