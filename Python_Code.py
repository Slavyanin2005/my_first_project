def get_user_name() -> str:
    """Запрашивает и возвращает имя пользователя с валидацией."""
    while True:
        name = input("Как тебя зовут? ").strip()
        if name.replace(' ', '').isalpha():
            return name
        print("Имя должно содержать только буквы. Попробуйте ещё раз.")


def greet_user() -> None:
    """Приветствует пользователя с персонализацией."""
    print("🌟 Добро пожаловать в программу-приветствие! 🌟")

    name = get_user_name()
    greeting = (
        f"Привет, {name}! Рад тебя видеть!"
        if len(name) > 2 else
        f"Привет, {name}! Короткое имя, но тоже отличное!"
    )
    print(greeting)


def show_menu() -> None:
    """Отображает меню дополнительных возможностей."""
    print("\nДоступные опции:")
    options = {
        '1': "Показать текущую дату",
        '2': "Сгенерировать случайное число",
        '0': "Выход"
    }
    for key, value in options.items():
        print(f"[{key}] {value}")


def main() -> None:
    """Основной цикл программы."""
    greet_user()

    while True:
        show_menu()
        choice = input("\nВыберите действие: ").strip()

        if choice == '1':
            from datetime import datetime
            print(f"Сегодня: {datetime.now().strftime('%d.%m.%Y')}")
        elif choice == '2':
            from random import randint
            print(f"Случайное число: {randint(1, 100)}")
        elif choice == '0':
            print("До новых встреч! 👋")
            break
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()