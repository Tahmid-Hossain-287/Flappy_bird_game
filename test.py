def this():
    new = 50

    while True:
        new -= 1
        print(new)
        if new <= 50:
            print("good")
        if new == 10:
            print("finished")
            return

this()
