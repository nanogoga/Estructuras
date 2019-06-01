
def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        raise ValueError(f'no existe el factorial'
                         f'para {num}'
                         )
    return num * factorial(num - 1)