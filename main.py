
# from csv import reader
# import xml.etree.ElementTree as ET

# tam = []
# with open('books-en.csv','r', encoding='windows-1251') as book:
#     tam = book.readlines()


# # amount of lines
# t = 0
# for i in tam:
#     if len(i.split(';')[1]) > 30:
#         t = t+1
# print(t)



# # search for author
# name = input('what are you searching for: ')
# for i in tam:
#     if name in i.split(';')[3] or name in i.split(';')[4]:
#         print(i.split[1])


# # #links to the 20 books
# with open('result.txt','w', encoding='windows-1251') as link :
#     for i in range(20):
#             link.write(tam[i].split(';')[1] + '. ' + tam[i].split(';')[2] +' - ' + tam[i].split(';')[3] + '\n')



# import csv
# import xml.etree.ElementTree as ET

# flag = 0
# output = open('result.txt', 'w')
# search = input('Search for: ')
# xml_output = ET.Element('currency_dict')

# with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
#     table = csv.reader(csvfile, delimiter=';')
#     for row in table:
#         lower_case = row[2].lower()
#         index = lower_case.find(search.lower())
#         price = float(row[8].replace(',', '.'))  # Assuming the price is in the 9th column (index 8)

#         if index != -1 and price <= 200:
#             print(row[2])
#             flag = 1
#             output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

#             # Create an XML element for each book with NumCode and Charcode
#             book_element = ET.SubElement(xml_output, 'book')
#             num_code_element = ET.SubElement(book_element, 'NumCode')
#             num_code_element.text = row[4]  # Assuming NumCode is in the 5th column (index 4)
#             char_code_element = ET.SubElement(book_element, 'Charcode')
#             char_code_element.text = row[5]  # Assuming Charcode is in the 6th column (index 5)

#     if flag == 0:
#         print('Nothing found.')

# # Save the XML tree to a file
# xml_tree = ET.ElementTree(xml_output)
# xml_tree.write('currency_dict.xml')

# output.close()







