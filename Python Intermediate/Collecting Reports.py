def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input());