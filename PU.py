# LIST
# x = [2,"a", 6, 7, "d"]

# for i in x:
#     print(i)

# print(len(x))

# print(x)
# x[3] = 9
# print(x)

# TUPLE

# b = ("cars", "houses", "money")
# b[-3] = "Benz C300"
# print(b[-3])


# DICTIONARY

# words = {
#     "noun":"A name of person, place, animal or thing",
#     "computer": "An Electronic Machine....",
#     "dictionary":"A book containing words and their meanings in ... "

# }


# print(words["dictionary"])

# SET

# x = (2,3,4,5,7)


# print(list(range(10)))

# for x in range(1,11):
#     print(str(x) + ". I am a Software Developer!.")


# ADMISSION CHECKER

# score = int(input("Enter your JAMB/UTME Score HERE:  \n"))

# if(score>=180):
#     print("Congratulations you are eligible for Admission")
# else:
#     print("Sorry, you are not eligible for Admission")


# WHILE LOOP
# count = 1
# while count<=10:
#     if(count>5):
#         break
#     print(str(count) + ". Hello Class, I am a Software Developer!")
#     # count = count+1
#     count+=1


# file = open("lumilab.txt", "r")

# # next(file)
# print(file.read(17))

# file.close()

import csv


lga = input("Enter LGA in Katsina State:").upper()


with open("KATSINA.csv", "r") as file:
    csvreader = csv.reader(file)
    # next(csvreader)
    count = 0
    for i in csvreader:
        if i[2]==lga:
            count+=1
    print(f"The total Polling Units in {lga} is {count}")        
       

# with open('KATSINA.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
    



