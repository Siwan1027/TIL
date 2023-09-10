# baekjun problem no.18110

# import sys

num = input()

def check(num):
    if int(num) == 0:
        return
    else:
        if num == num[::-1]:
            print('yes')
        else:
            print('no')
        num = input()
        check(num)

check(num)



# num = input()
# def check(num):
#     if int(num) == 0:
#         return
#     else:
#         if len(num) % 2 == 1:
#             num1 = int(num[:round(len(num)/2)+1])
#             num2 = num[round(len(num)/2):]
#             num2 = int("".join(reversed(num2)))
#             print(num1,num2,'case1',round(len(num)/2))

#         else:
#             num1 = int(num[:round(len(num)/2)])
#             num2 = num[round(len(num)/2):]
#             num2 = int("".join(reversed(num2)))
#             print(num1,num2,'case2',round(len(num)/2))


#         if int(num1) == int(num2):
#             print('yes')
#         else:
#             print('no')
#         num = input()
#         check(num)

# check(num)
