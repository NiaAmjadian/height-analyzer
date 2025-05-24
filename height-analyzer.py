def skyline(*args):
    if not args:
        return 0
    return max(args)

user_input = input()
a = [int(x) for x in user_input.split()] 

print(skyline(*a))