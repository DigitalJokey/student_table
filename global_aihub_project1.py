import pandas as pd

print("Please enter the names of the parameters\nType 'DATA' when you are done")
col_names = []
while True: # tablodaki sütunların isimlerini belirlemece :D
  x = input()
  if x == "DATA" or x == "data" or x == "Data":
    print(f"\nEnter the corresponding values with indexed format into the database e.g. '0 {col_names[0]}' \nCareful here!! DON'T use commas")
    break
  col_names.append(x)

index_numbers = []
size = len(col_names)
for i in range(size): # index için list oluşturduk
  index_numbers.append(i)

guide_example = dict(zip(index_numbers,col_names))
print("Storing Order: ",guide_example)

table_rows = []
row_data = [None]*size

cont = 0

while True:
  
  while cont != "n" or cont != "N":
  #for m in range(3): # kaç satır olacağını input alabiliriz ya da çıkış koşulu ekleriz
    for n in range(size):
      entered_data = input()
      clasify = entered_data.split(" ") # veriyi ikili olarak toplayıp ayıklıyoruz
      row_data[int(clasify[0])] = clasify[1]
    print(row_data,type(row_data))
    table_rows.append(tuple(row_data))
    cont = input("do you want to continue entering data? (y/n)\n")
    if cont == "n" or cont == "N":
      break
  print(table_rows)
  break

big = len(table_rows) #3
small = len(table_rows[0]) #4

df_columns = []
columns = []

for k in range(big+1): # k=0,1,2
  for l in range(small-1): # l= 0,1,2
    columns.append(table_rows[l][k])
  df_columns.append(columns)
  columns = [] # her döngüde temizlemek gerekiyor.
print("Dataframe columns: ",df_columns,type(df_columns))

my_dict = {}
for m in range(len(col_names)):
  my_dict[col_names[m]] = df_columns[m]
print("Data in dictionary format: ",my_dict)

df = pd.DataFrame(my_dict)
print(df)

df.to_csv("MY_FIRST_CSV_FILE.csv")