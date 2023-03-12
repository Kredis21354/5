import requests
from colorama import Fore
import logging
class Person:
  def __init__ (self, nat, gen):
    r = requests.get("https://randomuser.me/api/?nat=" + nat + '&gender=' + gen)
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surename = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]
    self.phone = res["results"][0]["phone"]
    self.email = res["results"][0]["email"]
    self.nation = res["results"][0]["nation"]
    self.isMale = res["results"][0]["gender"] == "male"

  def print_person(self):
    if self.isMale:
      print(Fore.CYAN)
    else:
      print(Fore.MAGENTA)
    print(self.name)
    print(self.surename)
    print(self.age)
    print(self.phone)
    print(self.email)
    print(self.nation)
    print(self.isMale)



pracivnyky = []

try:
  a = input('Скільки потрібно робітників для компанії?')
  a = int(a)
except:
  logging.warning
  a = input('Скільки потрібно робітників для компанії?')
  a = int(a)






m = input('Тільки чоловіки?')

gen = "male"

if m == "-":
  gen = "female"



while a != 0:
  n = input("Введіть національність")
  p = Person(n, gen)
  pracivnyky.append(p)
  a -= 1

for p in pracivnyky:
  p.print_person()































    
#random_person = Person('dk')
#random_person.print_person()

#try:
  #person2 = Person()
  #person2.print_person()
#except:
  #print('Не можу створити персону')




#if random_person.isMale:
  #print(Fore.CYAN)
#else:
  #print(Fore.MAGENTA)
#print(random_person.name)
#print(random_person.surename)
#print(random_person.age)
#print(random_person.phone)
#print(random_person.email)
#print(random_person.isMale)
