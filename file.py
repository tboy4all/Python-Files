# Working with files

# with open('first.txt', 'w') as file:
#     file.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos molestias ea sit veniam, rerum, totam quis eaque excepturi aut, nostrum reiciendis. At, harum quos adipisci magni nesciunt aliquid beatae sit!')

# with open('first.txt', 'r') as file:
#     print(file.read())

# with open('first.txt', 'r+') as file:
#     file.write("\nI'm at the beginning\n")
#     file.seek(100)
#     file.write("\nI'm in the middle\n")
#     file.seek(0)
#     print(file.read())

# with open('first.txt', 'a+') as file:
#     file.write("\nI'm at the end\n")
#     file.seek(0)
#     print(file.read())

# with open('first.txt', 'w+') as file:
#     file.write("Now everything is overwritten :(")
#     file.seek(0)
#     print(file.read())

# Working with File i/o with CSV And tsv

#import csv

# with open('file.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter='|')
#     rows = list(reader)
#     for row in rows:
#         print(', '.join(row)) 

# Using Dictionary to create row instead of a list

import csv

# with open('file.csv') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter='|')
#     rows = list(reader)
#     for row in rows:
#         print(row)

# Writing in lists form using csv
# with open('file.csv', 'a') as csvfile:
#     data_writer = csv.writer(csvfile, delimiter="|")
#     data_writer.writerow(['Gab','Cattle','55'])

# # Reading in List form using csv
# with open('file.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter='|')
#     rows = list(reader)
#     for row in rows:
#         print(', '.join(row)) 

# # Writing in Dictionaries form using csv

# with open('newfile.csv', 'a') as csvfile:
#     data = ['name', 'fav_topic']
#     writer = csv.DictWriter(csvfile, fieldnames=data)
#     writer.writeheader() # this writes the first row with the column headings
#     writer.writerow({
#         'name': 'Elie',
#         'fav_topic': 'Writing to CSVs!'     
#     })


#     def gensquares(n):
#         for num in range(n):
#             yield num**2

# for x in gensquares(10):
#     print(x)


# def fib_with_generator(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#          # a,b = b, a+b -> tuple unpacking instead of the three lines below!
#         temp = a
#         a = b
#         b = temp + b

# for num in fib_with_generator(10):
#     print(num)

# Using Next function

def use_next():
#     for x in range(10):
#         yield x

# # gen = use_next()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# for val in use_next():
#     print(val)

#       OR

    return print((x for x in range(10)))
