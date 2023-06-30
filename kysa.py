while True:
    password = input("Введите пароль:")
    if 8>len(password) or len(password)>20:
        print("Ошибка: длина пароля должна быть от 8 до 20 символов.")
    elif not any(char.isdigit() for char in password):
        print("Ошибка: пароль должен содержать хотя бы одну цифру.")
    elif not any(char.islower() for char in password):
        print("Ошибка: пароль должен содержать хотя бы одну строчную букву.")
    elif not any(char.isupper() for char in password):
        print("Ошибка: пароль должен содержать хотя бы одну заглавную букву.")
    elif not any(char in "!#$%&'()*,-./:;<=>?@{\}~^_[+]|" for char in password):
        print("Ошибка: пароль должен содержать хотя бы один специальный символ.")
    else:
        print("Пароль верный.")
        break



