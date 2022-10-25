def decorator(func):
    def inner(*args, **kwargs):
        arg = ', '.join(str(i) for i in args)
        if kwargs:
            print(f"{func.__name__} called with {kwargs}")
        else:
            print(f"{func.__name__} called with {arg}")
    return inner


@decorator
def say(name, surname):
    return f"{name} {surname}"


@decorator
def pow_all(nums):
    return [int(i)**2 for i in nums]


num = [1, 2, 3, 4, 5]

say("Vlad", "Khimich")
pow_all(num)
