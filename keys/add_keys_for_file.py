from config import *
import csv

file = open(r"keys/keys.csv", "r")
data = list(csv.reader(file, delimiter=","))

print(list_home) # выводи сообщение без новой строки 
num_home = int(input())

for list in data:
    keys = list[1]
    apartment = list[0]
    apartment = int(apartment)
    
    cycle_keys(keys,num_home,apartment)
        
