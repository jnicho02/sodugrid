import csv
import requests

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7ieQIz2CYpX40jdgeHsqCnM7wqjgT1GpqirqotBgtYgtHZSrAeqf8DFJjLvk__fMFa9PdR9S_gnKc/pub?gid=11&single=true&output=csv"

response = requests.get(url, timeout=10)

lines = list(line.decode('utf-8') for line in response.iter_lines())
csv_reader = csv.reader(lines, delimiter=',')

for row in csv_reader:
    print(row)
