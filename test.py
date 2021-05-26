new = 50

var = "test"
def one():
    # global var
    print(var)

def two():
    # global var
    print(var)
    clone_of_var = var
    while True:
        print(var)

one()
two()
