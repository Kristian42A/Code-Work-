import pandas as pd
import matplotlib.pyplot as plot


data = [
    ["Company", "Score"],
    ["Amazon", 80],
    ["Netflix", 70],
    ["Apple", 95],
    ["Roche", 100],
    ["Samsung", 75],
    ["Migros", 50],
    ["Playstation", 90],
    ["FIFA", 100],
    ["Walmart", 90],
    ["AliExpress", 20],
    ["Target", 40],
    ["Aldi", 75],
    ["Lidl", 60],
    ["Nintnedo", 55],
    ["Xboc", 50],

]


file_path = 'input.txt'


with open(file_path, mode='w') as file:
    for row in data:
        file.write(','.join(map(str, row)) + '\n')

print(f'Data has been written to {file_path}')


data = pd.read_csv(file_path)


print(data)


plot.figure(figsize=(10, 6))
plot.bar(data['Company'], data['Score'], color='skyblue')
plot.xlabel('Company')
plot.ylabel('Score')
plot.title('Company Scores')
plot.xticks(rotation=45)
plot.show()
