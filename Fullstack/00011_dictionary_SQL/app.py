
import mysql.connector

con = mysql.connector.connect(
user ="ardit700_student",
password ="ardit700_student",
host= "108.167.140.122",
database ="ardit700_pm1database"
)
cursor = con.cursor()

word = input('Enter a word and search the database: ')
strquery = "SELECT * FROM Dictionary WHERE Expression= '%s'  "% word

query = cursor.execute(strquery)
results = cursor.fetchall()

print(results)

if results:
    for result in results:
        print(result)
else:
    print("No results found")



# #Datasource
# import json
# import difflib
# from difflib import SequenceMatcher
# from difflib import get_close_matches

# dictionary = json.load(open("data.json"))

# #print(dictionary.keys())
# word_list = dictionary.keys()
# print(type(word_list))
# print('yann'.upper())


# def check_similarity(word):

#     similar = get_close_matches(word, word_list)
#     if len(similar)> 0:
#         return "Did you mean %s" %get_close_matches(word, word_list)[0]
#     else:
#          return "The word does not exist. Please double check it"


# def definition(word):
#         word = word.lower()
#         if(word in word_list):
#             return dictionary[word]
#         elif(word.title() in word_list):
#             return dictionary[word.title()]
#         elif(word.upper() in word_list):
#             return dictionary[word.upper()]

#         elif(len(get_close_matches(word, word_list)))> 0:
#             # return "Did you mean %s ? Enter Y for yes or N for no." %get_close_matches(word, word_list)[0]
#             yesno_input = input("Did you mean %s ? Enter Y for yes or N for no." %get_close_matches(word, word_list)[0])
#             if(yesno_input.lower() =='y'):
#                 return dictionary[get_close_matches(word, word_list)[0]]
#             elif(yesno_input.lower() =='n'):
#                 return "The word does not exist."
#             else:
#                 return "We did not understand your query."
#         else:
#             return "The word does not exist. Please double check it."



# while True:
#     user_input = input("Enter a word: ")

#     # print(definition(user_input))
#     output = definition(user_input)
#     if(type(output)== list):
#         for item in output:
#             print(item)

#     #print(output)


