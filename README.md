# iBook
"Персональний помічник" з інтерфейсом командного рядка. 

## Функціонал: 
- Додавання нових користувачів (ім'я, день народження, телефони, адреса)
- Пошук користувачів по різних критеріях
- Додавання нотатків з тагами
- Пошук нотатків
- Використання штучного інтелекту для пошуку інформації

## Встановлення

### Використовуючи вихідний код

1. Стягніть код з github
2. Якщо плануєте користуватись AI, створіть env file, і помістіть туди ключ ```OPENAI_API_KEY```.
3. Щоб запустити проект скористайтесь командою ```pip install -e .``` з кореневої папки. І далі в консолі запустіть програму командою: ```run_book```
Інший шлях для запуску: ```python3 iBook/main.py```.

### Використовуючи pypi

Для встановлення пакету виконайте команду: ```pip install iBook```
Щоб запустити команду з AI помічником потрібно вказати ключ OpenAI: ```run_book --open-ai-key=```

## Архітектура проекту

## Структура

## Збірка проекту і завантаження на pypi

1. Переконайтесь, що у Вас створений обліковий запис на pypi
2. Зберіть застосунок: ```python setup.py sdist```
3. Завантажте застосунок на pypi: ```twine upload dist/*```

## Тестування

Для тестування проекту виконайте ```pytest iBook/tests```

