import os

tasks = []

def show_tasks():
    task_number = 1
    for task in tasks:
        print(str(task_number) + ". " + task)
        task_number += 1

def add_task():
    task_number = 1
    if len(tasks) > 0:
        for i in tasks:
            print(f"{task_number}. {i}")
            task_number += 1

    task = input("Wpisz zadanie do zrobienia: ")
       # nie udaje mi się sprawdzić czy to string - zmienić to
    while True:
        ind = int(input("Pod jak jakim numerem dać zadanie: "))
        if ind > 0 and ind <= len(tasks) + 1:
            with open("data3.txt", "a") as file:
                file.write(task + "\n")
            tasks.insert(ind-1, task)
            print("Zadanie dodane!")
            break
        else:
            print("Błędna wartość. Spróbuj ponownie")
            continue
            
def del_task():
    task_number = 1 
    for i in tasks:
        print(f"{task_number}. {i}")
        task_number += 1
    try:
        task_number = int(input("Podaj numer zadania do usunięcia: "))
        if (task_number) > 0 and task_number <= len(tasks):
            with open('data3.txt', 'r') as first:
                with open('temp.txt', 'w') as second:
                    for line in first:
                        if tasks[task_number - 1] not in line.strip("\n"):
                            second.write(line)
            x = tasks.pop(task_number - 1)
            print(f"Usunięto następujące zadanie: {x}")  
            os.replace("temp.txt", 'data3.txt') 
        else:
            raise ValueError
    except ValueError:
        print(f"{task_number} jest błędną wartością, spróbuj ponownie!")
        del_task()

def load_file():
    print('\n')
    with open("data3.txt") as file:
        newline = ""
        for readline in file:
            newline += readline
        print(newline)

while True:
    print("\nCo chcesz zrobić?:")
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wczytaj plik")
    print("5. Wyjdź")
    
    try:
        user_choice = int(input("Wybierz liczbę: "))
        if user_choice == 1:
            print("\n")
            show_tasks()
        elif user_choice == 2:
            add_task()
        elif user_choice == 3:
            if len(tasks) == 0:
                print("Nie ma żadnego zadania do usunięcia")
                continue
            else:
                del_task()
        elif user_choice == 4:
            if len(tasks) == 0:
                print('Plik data3.txt jest pusty')
                continue
            else:
                load_file()
        elif user_choice == 5:
            with open("data3.txt", 'r+') as file:
                print("Koniec programu. Dane z pliku data3.txt zostaną usunięte")
                file.truncate()
                break
    except ValueError:
        print("Błędna wartość! Spróbuj ponownie")
        continue