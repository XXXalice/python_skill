def palindrome(text):
    odd_switch = 1 if len(text)/2 == 0 else 0
    harff = text[:int(len(text)/2)]
    harfs = text[int(len(text)/2)+odd_switch:]
    judge = True if harff == ''.join(harfs[::-1]) else False
    return judge

