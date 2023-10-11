import requests
import json
from config import *
import csv

file = open(r"keys\keys.csv", "r")
data = list(csv.reader(file, delimiter=","))

print (data[1][1])