import random
########################Task 1########################
# def unique(l):
#     return list(set(l))
# print(unique([1,2,1,2,3]))

########################Task 2########################
# def formatter(str1, str2):
#     l1 = len(str1)
#     l2 = len(str2)
#     return f"{str1[:round(l1/2)+1]}{str2[:round(l2/2)+1]}{str1[round(l1/2)+1:]}{str2[round(l2/2)+1:]}"
# print(formatter("abcde", "fghij"))

########################Task 3########################
# def isDiff(li):
#     return len(li) == len(set(li))
# print(isDiff([1,2,3,4,4]))

########################Task 4########################
# def bubbleSort(li):
#     li_len = len(li)
#     for i in range(li_len):
#         for j in range(i, li_len):
#             if (li[i] > li[j]):
#                 li[i], li[j] = li[j], li[i]
#     return li
# print(bubbleSort([5,4,3,2,1]))

########################Task 5########################
# def game():
#     number = random.randint(0, 100)
#     guesses = set()
#     trials = 10
#     i = 1

#     while i <= trials:
#         print(10*"-", f" try {i} of {trials} ",10*"-")
#         guess = int(input("Enter a number: "))
#         if guess > 100:
#             print("your guess is out of range from 0, to 100")
#             i -= 1
#         elif guess in guesses:
#             print("you have already tried this guess before")
#             i -= 1
#         elif guess < number:
#             print("your guess is less than the number")
#         elif guess > number:
#             print("your guess is more than the number")
#         else:
#             print("Congrats, you are right\nNow Guess Again!")
#             number = random.randint(0, 100)
#         i += 1
#         guesses.add(guess)

# game()
# while True:
#     print("Do you want to play again?\n1\tyes\n2\tno")
#     response = int(input("Enter your choice: "))
#     if response == 1:
#         game()
#     elif response == 2:
#         break
#     else:
#         print("Please choose one from 1 and 2")