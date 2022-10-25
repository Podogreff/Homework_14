def stop_words(words: list):
    def inner_x(func):
        def inner(*args, **kwargs):
            lst = []
            for i in func(*args, **kwargs).strip('!').split():
                if i in words:
                    lst.append("*")
                else:
                    lst.append(i)
            return " ".join(lst) + "!"

        return inner

    return inner_x


@stop_words(["pepsi", 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his new BMW!"


print(create_slogan("Vlad"))

