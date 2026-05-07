import json
import os
file_name="expense.json"
def load_data():
    if not os.path.exists(file_name):
        return[]
    with open(file_name, "r") as file:
        return json.load(file)
def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
#def get_categories(data):
#    categories = set()
#    for item in data:
 #       categories.add(item["category"])
 #   return list(categories)
def add_expense(data, category, price, user_id):
    #categories = get_categories(data)
   # if  categories:
        #print("\n Выбери категорию или введи новую:")
        #for i, cat in enumerate(categories, 1):
           # print(f"{i}. {cat}")
       ## print("0. Новая категория")
        #choice = input("Выбор: ")
        #if choice == "0":
        #    category = input("Новая категория: ")
        #else:
         #   try:
         #       category = categories[int(choice) - 1]
          #  except:
           #     print("Ошибка выбора")
           #     return
   # else:
      #  category = input("Категория: ")
   # try:
     #   price = float(input("Цена: "))
   # except:
     ##  return
    expense = {
        "category": category,
        "price": price,
        "user_id": user_id
    }
    data.append(expense)
    save_data(data)
    print("Расход добавлен")
def show_expenses(data):
    if not data:
        print("Расходов нет")
        return
    for item in data:
        print(f"{item['category']} - {item['price']}")
def show_sum(data):
    sum=0
    for item in data:
        sum+=item['price']
    print("Общая сумма:", sum)
#def main():
    #data=load_data()
    #while True:
      #  print("\n1. Добавить расход")
      #  print("2. Показать расходы")
       # print("3. Общая сумма расходов")
       # print("4. Выход")
        #choice = input("Выбор:")
        #if choice == "1":
        #    add_expense(data)
       # elif choice == "2":
       #     show_expenses(data)
        #elif choice == "3":
        #    show_sum(data)
       # elif choice == "4":
        #    break
        #else:
           # print("Ошибка")
#if __name__ == "__main__":
   # main()