
from csv import reader

tam = []
with open('books-en.csv','r', encoding='windows-1251') as book:
    tam = book.readlines()


# amount of lines
t = 0
for i in tam:
    if len(i.split(';')[1]) > 30:
        t = t+1
print(t)



# search for author
name = input('search for: ')
for i in tam:
    if name in i.split(';')[3] or name in i.split(';')[4]:
        print(i.split[1])


#links to the 20 books
with open('result.txt','w', encoding='windows-1251') as tameem :
    for i in range(20):
            tameem.write(tam[i].split(';')[1] + '. ' + tam[i].split(';')[2] +' - ' + tam[i].split(';')[3] + '\n')






# flag = 0
# output = open('result.txt', 'w')
# search = input('Search for: ')
# with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
#     table = reader(csvfile, delimiter=';')
#     for row in table:
#         lower_case = row[2].lower()
#         index = lower_case.find(search.lower())
#         if index != -1:
#             print(row[2])
#             flag = 1
#             output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

#     if flag == 0:
#         print('Nothing found.')

# output.close()