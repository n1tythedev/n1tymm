def NumberCheck(number):
    try:
        testv = float(number)
        return True
    except ValueError:
        return False
def InitializationOfApp(Name, Version):
    print("Initialization...")
    print(Name)
    print("By N1tyTheDev")
    print(f"Version {Version}")
    print("MMVersion 1.0")
    print("Initialization Complete.")