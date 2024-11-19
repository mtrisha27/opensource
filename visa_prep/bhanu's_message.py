def is_valid(num):
    if num.startswith('+'):
        part=num.split()
        if len(part)==2:
            code=part[0][1:]
            n=part[1]
            if len(code) in (0,2) and len(n)==10 and n.isdigit():
                if sum(int(digit) for digit in n)>0:
                    return "Correct"
    elif len(num)==10 and num.isdigit():
        if sum(int(digit) for digit in num)>0:
            return "Correct"
    return "Incorrect"
num=input()
print(is_valid(num))
