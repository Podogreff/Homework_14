
def arg_rules(type_: type, max_length: int,  contains: []):
    def inner(func):
        def wrapper(some):
            if isinstance(some, type_):
                if len(some) < max_length:
                    if all([i in str(some) for i in contains]):
                        return func(some)
                    else:
                        print(False)
                        print(f"Text should contains {contains} symbols")
                else:
                    print(False)
                    print("The length should be less then the specified ")
            else:
                print(False)
                print("Please enter a string type!")

        return wrapper
    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    print(f"{name} drinks pepsi in his new BMW!")


create_slogan("05@a321121323fsf54142")