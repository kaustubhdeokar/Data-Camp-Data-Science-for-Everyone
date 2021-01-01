def raise_val(n):
    inner = 0
    def inner(x):
        raised = x**n
        return raised
    return inner

square=raise_val(2)
cube=raise_val(3)


raise_val(2)(3)#9
