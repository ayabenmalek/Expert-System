from aima.logic import *
from aima.utils import *
import sys
import re


input_data = sys.argv[1:]
with open('data.txt', 'w') as file:
    file.write(f"{input_data}\n")
input_string = (f"{input_data}")
match = re.search(r"\['(.*)'\]", input_string)
if match:
    values = match.group(1)  
    mealtype, preference, occasion = values.split(',')
    b=type(mealtype)
    with open('data.txt', 'w') as file:
        file.write(f"{b}\n")
else: 
    with open('data.txt', 'w') as file:
        file.write(f"erre\n")




kb = FolKB()
kb.tell(expr('Maindish(x) & Nospecific(x) & Party(x) ==> Spaghetti(x)'))
kb.tell(expr('Maindish(x) & Nospecific(x) & Anniversary(x) ==> Sushi(x)'))
kb.tell(expr('Maindish(x) & Dairyfree(x) & Repasrapide(x) ==> Quichewitheggsonly(x)'))
kb.tell(expr('Maindish(x) & Vegan(x) & Repasrapide(x) ==> VegetarianPizza(x)'))
kb.tell(expr('Maindish(x) & Nospecific(x) & Anniversary(x) ==> SeafoodPlatter(x)'))
kb.tell(expr('Appetizer(x) & Glutenfree(x) & Party(x) ==> CaesarSalad(x)'))
kb.tell(expr('Appetizer(x) & Nospecific(x) & Party(x) ==> CheesePlatter(x)'))
kb.tell(expr('Appetizer(x) & Nospecific(x) & Repasrapide(x) ==> MiniHamburgers(x)'))
kb.tell(expr('Dessert(x) & Nospecific(x) & Anniversary(x) ==> FruitSalad(x)'))
kb.tell(expr('Dessert(x) & Glutenfree(x) & Party(x) ==> Cupcakes(x)'))
kb.tell(expr('Dessert(x) & Vegan(x) & Party(x) ==> FruitTart(x)'))
kb.tell(expr('Dessert(x) & Nospecific(x) & Party(x) ==> Cheesecake(x)'))
kb.tell(expr('Maindish(x) & Glutenfree(x) & Party(x) ==> FishTacos(x)'))
kb.tell(expr('Dessert(x) & Nospecific(x) & Repasrapide(x) ==> CarrotCake(x)'))
kb.tell(expr('Appetizer(x) & Vegan(x) & Party(x) ==> GreekSalad(x)'))
kb.tell(expr('Maindish(x) & Glutenfree(x) & Repasrapide(x) ==> CornSoup(x)'))

selected_Options = [mealtype, preference, occasion]
with open('data.txt', 'w') as file:
        file.write(f"{type(selected_Options)}\n")
dish = expr('dish')
agenda = [expr(option + '(dish)') for option in selected_Options]
memory = {}
seen = set()



while agenda:
    p = agenda.pop()
    
    if p in seen:
        continue
    seen.add(p)
    if fol_fc_ask(kb, p):
        memory[p] = True
    else:
        memory[p] = False
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('Spaghetti(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Anniversary(dish)'), False)):
        agenda.append(expr('Sushi(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Dairyfree(dish)'), False) and memory.get(expr('Repasrapide(dish)'), False)):
        agenda.append(expr('Quichewitheggsonly(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Vegan(dish)'), False) and memory.get(expr('Repasrapide(dish)'), False)):
        agenda.append(expr('Vegetarian Pizza(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Anniversary(dish)'), False)):
        agenda.append(expr('SeafoodPlatter(dish)'))
    if (memory.get(expr('Appetizer(dish)'), False) and memory.get(expr('Glutenfree(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('CaesarSalad(dish)'))
    if (memory.get(expr('Appetizer(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('CheesePlatter(dish)'))
    if (memory.get(expr('Appetizer(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Repasrapide(dish)'), False)):
        agenda.append(expr('MiniHamburgers(dish)'))
    if (memory.get(expr('Dessert(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Anniversary(dish)'), False)):
        agenda.append(expr('FruitSalad(dish)'))
    if (memory.get(expr('Dessert(dish)'), False) and memory.get(expr('Glutenfree(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('Cupcakes(dish)'))
    if (memory.get(expr('Dessert(dish)'), False) and memory.get(expr('Vegan(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('FruitTart(dish)'))
    if (memory.get(expr('Dessert(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('Cheesecake(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Glutenfree(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('FishTacos(dish)'))
    if (memory.get(expr('Dessert(dish)'), False) and memory.get(expr('Nospecific(dish)'), False) and memory.get(expr('Repasrapide(dish)'), False)):
        agenda.append(expr('Flan(dish)'))
    if (memory.get(expr('Appetizer(dish)'), False) and memory.get(expr('Vegan(dish)'), False) and memory.get(expr('Party(dish)'), False)):
        agenda.append(expr('GreekSalad(dish)'))
    if (memory.get(expr('MainDish(dish)'), False) and memory.get(expr('Glutenfree(dish)'), False) and memory.get(expr('Repasrapide(dish)'), False)):
        agenda.append(expr('CornSoup(dish)'))



result = []
for p, value in memory.items():
    if value and str(p).startswith(('Spaghetti', 'Sushi','Quichewitheggsonly' ,'VegetarianPizza','SeafoodPlatter','CaesarSalad','CheesePlatter','MiniHamburgers','FruitSalad','Cupcakes','Cheesecake','FishTacos','CarrotCake','GreekSalad','CornSoup')):
        meal = str(p).split('(')[0]
        result.append(meal)
with open('data.txt', 'w') as file:
        file.write(f"{type(result)}\n")
print(result)