import random
import json #uvozimo knjižnico za json
import datetime

secret=random.randint(1,20)
attempts=0
name=str(input("Kako ti je ime?"))

with open("records.json","r") as records_file:
   records_list=json.loads(records_file.read())

   top_records = sorted(records_list, key=lambda x: x["attempts"])[:3]  #s tem sortiraš slovarje po attempts

   for dict in top_records[:3]:   #šli bomo čez seznam slovarjev v .json fajlu in bomo šli samo do tretjega
      print(f"{dict["attempts"]} attempts, date: {dict["date"]}, igralec: {dict["name"]}, skrivna stevilka: {dict["sic_num"]}")

while True:
    guess=int(input("Ugani številko: "))
    attempts+=1
   
    if guess==secret:
      time=str(datetime.datetime.now()) #datum in uro spremenim v niz
      records_list.append({"attempts": attempts, "date": time, "name": name, "sic_num": secret}) #dodali bomo naše poskuse in jih zapisal v json datoteko
      with open ("records.json","w") as records_file:
         records_file.write(json.dumps(records_list))
   
      print("Bravo")
      break
    elif guess>secret:
       print("Vnesi nižjo številko")
    elif guess<secret:
       print("Poskusi višjo številko")
    else:
      print("Ups, ni ti ratalo")

