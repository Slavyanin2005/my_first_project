def get_user_name() -> str:
    """Запрашивает и возвращает имя пользователя с валидацией."""
    while True:
        name = input("Как тебя зовут? ").strip()
        if name and name.replace(' ', '').isalpha():
            return name.title()  # Первая буква заглавная
        print("Ошибка: имя должно содержать только буквы и не быть пустым. Попробуйте ещё раз.")


def greet_user() -> None:
    """Приветствует пользователя с персонализацией."""
    print("\n🌟 Добро пожаловать в программу-приветствие! 🌟")
    print("(Введите 0 в меню для выхода)\n")

    name = get_user_name()
    greeting = (
        f"Привет, {name}! Рад тебя видеть!"
        if len(name) > 2 else
        f"Привет, {name}! Минимум букв - максимум личности!"
    )
    print(greeting)


def show_menu() -> None:
    """Отображает меню дополнительных возможностей."""
    print("\nДоступные опции:")
    options = {
        '1': "Показать текущую дату",
        '2': "Сгенерировать случайное число (1-100)",
        '0': "Завершить программу"
    }
    for key, value in options.items():
        print(f"  {key}. {value}")


def main() -> None:
    """Основной цикл программы."""
    greet_user()

    while True:
        show_menu()
        choice = input("\nВаш выбор: ").strip()

        if choice == '1':
            from datetime import datetime
            print(f"\nСегодня: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
        elif choice == '2':
            from random import randint
            num = randint(1, 100)
            print(f"\nВаше случайное число: {num} {'(удачное!)' if num > 90 else ''}")
        elif choice == '0':
            print("\nСпасибо за использование программы! До новых встреч! 👋\n")
            break
        else:
            print("\n⚠ Неизвестная команда. Пожалуйста, выберите вариант из меню.")


if __name__ == "__main__":
    main()