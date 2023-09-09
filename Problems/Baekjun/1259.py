# baekjun problem no.18110

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