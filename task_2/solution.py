import csv
import pandas as pd

# variables
inputItem = 0

header = ['No', 'task', 'status']
tasks = []
status = 'not done'

# functions


def add_an_item(status):
    task = str(input("Enter your task: "))

    with open('tasks.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        rowCount = 0
        for row in reader:
            rowCount += 1
            # print(rowCount)

    with open('tasks.csv', 'a', encoding="UTF8", newline='') as f:
        writer = csv.writer(f)
        tasks.append(task)

        if rowCount == 0:
            data = [1, task, status]
        data = [rowCount, task, status]
        writer.writerow(data)


def remove_an_item():
    task = str(input("Enter number of task to remove: "))

    lines = list()
    with open('tasks.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == task:
                    lines.remove(row)
                    print("Your task was removed!")

    with open('tasks.csv', 'w', encoding="UTF8", newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


def mark_an_item_as_done():
    task = int(input("Enter number of task which is done: "))

    df = pd.read_csv("tasks.csv")

    # updating the column value
    for i in range(len(df)):
        if task == df["No"][i]:
            df.loc[i, 'status'] = 'Done'

    # writing into the file
    df.to_csv("tasks.csv", index=False)

    print("Your task was done!")


def list_items():
    with open('tasks.csv', 'r') as f:
        reader = csv.reader(f)
        print("All items: ")
        for row in reader:
            print(row)


def add_multiple_items(status):
    amountOfItems = int(input("Enter amount of items: "))

    for i in range(0, amountOfItems):
        task = str(input("Enter your task: "))

        with open('tasks.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            rowCount = 0
            for row in reader:
                rowCount += 1
                # print(rowCount)

        with open('tasks.csv', 'a', encoding="UTF8", newline='') as f:
            writer = csv.writer(f)
            tasks.append(task)

            if rowCount == 0:
                data = [1, task, status]
            data = [rowCount, task, status]
            writer.writerow(data)


def remove_multiple_items():
    amountOfTasks = int(input("Enter amount of tasks to remove: "))

    tasks = []

    for i in range(0, amountOfTasks):
        task = str(input("Enter numbers of tasks to remove: "))
        tasks.append(task)

    # df = pd.read_csv("tasks.csv")

    # print(df['No'][2])
    # # deleting the columns
    # for i in range(0, amountOfTasks):
    #     if tasks[i] == df["No"][i]:
    #         df.drop[i]
    #         print(df)

    # # writing into the file
    #         df.to_csv("tasks.csv", index=False)

    lines = list()
    with open('tasks.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                for item in tasks:
                    if field == item:
                        lines.remove(row)
                        print("Your task was removed!")

    with open('tasks.csv', 'w', encoding="UTF8", newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    print("Your task was done!")


while(inputItem != 7):
    # Printing menu
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Mark an item as done")
    print("4. List items")
    print("5. Add multiple items")
    print("6. Remove multiple items")
    print("7. Exit")

    inputItem = int(input("Enter number: "))

    if inputItem == 1:
        print("You chose add an item")
        add_an_item(status)
    elif inputItem == 2:
        print("You chose remove an item")
        remove_an_item()
    elif inputItem == 3:
        print("You chose mark an item as done")
        mark_an_item_as_done()
    elif inputItem == 4:
        print("You chose list items")
        list_items()
    elif inputItem == 5:
        print("You chose add multiple items")
        add_multiple_items(status)
    elif inputItem == 6:
        print("You chose remove multiple items")
        remove_multiple_items()
    else:
        break
