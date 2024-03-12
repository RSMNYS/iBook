from notes import Notebook, NotebookSearcher

def main():
    
    #Створює нову нотатку

    notebook = Notebook()

    while True:
        print("\nМеню:")
        print("1. Додати нотатку")
        print("2. Редагувати нотатку")
        print("3. Видалити нотатку")
        print("4. Пошук за заголовком")
        print("5. Пошук за тегом")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            title = input("Введіть заголовок нотатки: ")
            content = input("Введіть контент нотатки: ")
            notebook.add_content(title, content)
            tags_input = input("Введіть теги (через кому): ")
            tags = [tag.strip() for tag in tags_input.split(",")]
            for tag in tags:
                notebook.add_tags(tag)

        elif choice == "2":
            title = input("Введіть заголовок нотатки, яку потрібно редагувати: ")
            new_content = input("Введіть новий контент: ")
            notebook.edit_content(title, new_content)

        elif choice == "3":
            title = input("Введіть заголовок нотатки, яку потрібно видалити: ")
            notebook.delete_notebook(title)

        elif choice == "4":
            query = input("Введіть запит для пошуку за заголовком: ")
            results = NotebookSearcher(notebook).search_by_title(query)
            if results:
                print("Результати пошуку:")
                for result in results:
                    print(f"Заголовок: {result[0]}")
                    print(f"Контент: {result[1]}")
                    print(f"Теги: {result[2]}")
            else:
                print("Нотаток не знайдено за введеним запитом.")

        elif choice == "5":
            tag = input("Введіть тег для пошуку: ")
            results = NotebookSearcher(notebook).search_by_tag(tag)
            if results:
                print("Результати пошуку:")
                for result in results:
                    print(f"Заголовок: {result[0]}")
                    print(f"Нотатка: {result[1]}")
                    print(f"Теги: {result[2]}")
            else:
                print("Нотатку не знайдено за введеним тегом.")

        elif choice == "6":
            print("Дякую за використання програми!")
            break

        else:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 6.")


if __name__ == "__main__":
    main()
