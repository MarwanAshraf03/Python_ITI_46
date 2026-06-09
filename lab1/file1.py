########################Task 1########################
# first_name = input("First Name: ")
# second_name = input("Second Name: ")
# print(f"{second_name} {first_name}")

########################Task 2########################
# number = input("Enter Number: ")
# print(int(f"{number}") + int(f"{number}{number}") + int(f"{number}{number}{number}"))

########################Task 3########################
# heredoc_string = """a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example"""
# print(heredoc_string)

########################Task 4########################
# print(f"Volume of Sphere wit Radius of 6 is {(4/3) * (3.14) * pow(6, 3)}")

########################Task 5########################
# height = float(input("Enter the Height of the Triangle: "))
# base = float(input("Enter the base length of the Triangle: "))
# print(f"Area of the Triangle is {(1/2) * base * height}")

########################Task 6########################
# n = int(input("Enter number: "))
# for i in range(-n, n):
#     for j in range(n - abs(i)):
#         print("*", end="")
#     print()

########################Task 7########################
# word = input("Enter a word: ")
# reversed_word = ''
# for i in word:
#     reversed_word = i + reversed_word
# print(reversed_word)

########################Task 8########################
# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

########################Task 9########################
# n1 = 0
# n2 = 1
# n_temp = 0
# n_last = 50
# while True:
#     print(n2)
#     n_temp = n2
#     n2 = n1 + n2
#     n1 = n_temp
#     if (n2 >= n_last):
#         break

########################Task 10########################
# sentence = input("Enter a sentence: ")
# n_digits = 0
# n_letters = 0
# for i in sentence:
#     if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
#         n_letters += 1
#     if ord('0') <= ord(i) <= ord('9'):
#         n_digits += 1
# print(f"sentence: {sentence}, contains {n_letters} letters, and {n_digits} digits")
