from collections import UserDict

class Notebook(UserDict):

    #Клас який працює як нотатки, зберігає заголовок, контент та теги нотаток використовуючи UserDict

    def __init__(self, title = "Напишіть тут свій заголовок"):

        #Запускає програму нотатки, створює нотатку з дефолтним заголовком

        super().__init__()
        self.title = title
        self.tags = []

    def add_title(self, title): 

        #Добавляє заголовок

        self.title = title
        print("Заголовок додано!")

    def get_title(self):

        #Повертає заголовок

        return self.title
    
    def edit_title(self, new_title):

        #Змінює заголовок

        self.title = new_title
        print("Заголовок нотатки змінено!")

    def add_content(self, title, content):

        #Додає нотатку до коду

        self.data[title] = content
        print("Нотатку додано!")

    def get_content(self, title):

        #Повертає нотатку

        return self.data.get(title)
    
    def edit_content(self, title, new_content):

        #Якщо заголовок нотатки існує, то змінює контент нотатки

        if title in self.data:
            self.data[title] = new_content
        else:
            print(f"Помилка: Нотатка с заголовком '{title}' не знайдена.")

    def add_tags(self, tag):

        #Добавляє теги до нотатки

        self.tags.append(tag)
        print("Тег додано!")


    def get_tags(self):

        #Показує теги нотатки

        return self.tags
    
    def edit_tags(self, old_tag, new_tag):

        #Змінює теги нотатки якщо такий тег існує

        try:
            index = self.tags.index(old_tag)
            self.tags[index] = new_tag
            print("Тег змінено!")
        except ValueError:
            print(f"Помилка: Нотатка с тегом '{old_tag}' не знайдена.")
    
    def delete_notebook(self, title):

        #Видаляє нотатку якщо така нотатка існує

        if title in self.data:
            del self.data[title]
            print("Нотатка видалена успішно!")
        else:
            print(f"Помилка: Нотатка c заголовком '{title}' не знайдена.")
    
    def to_notebook(self):

        #Добавляє весь контент до нотатки

        return {
            "Заголовок" : self.title,
            "Нотатка" : self.data,
            "Теги" : self.tags
            }
    
class NotebookSearcher:

    def __init__(self, notebook):

        self.notebook = notebook

    def search_by_title(self, query):

        results = []
        for title, content in self.notebook.to_notebook()["Нотатка"].items():
            if query.lower() in title.lower():
                results.append((title, content, self.notebook.get_tags()))
        return results

    def search_by_tag(self, tag):

        results = []
        for title, content in self.notebook.to_notebook()["Нотатка"].items():
            if tag in self.notebook.get_tags():
                results.append((title, content, self.notebook.get_tags()))
        return results