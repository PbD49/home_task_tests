def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result


def check_email(email: str) -> bool:
    if "@" in email and "." in email and " " not in email:
        return True
    else:
        return False


def longest_film(films: str) -> str:
    longest_film_name = max(films, key=len)
    return longest_film_name


if __name__ == '__main__':
    auth = check_age(10)
    print('Возраст 10:', auth)
    auth = check_age(20)
    print('Возраст 20:', auth)

    email_valid = check_email('mail@mail.ru')

    list_films = ['Аладин', 'Мадагаскар', 'Бетховен']
    film = longest_film(list_films)
