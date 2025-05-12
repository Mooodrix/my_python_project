def hello(firstname="John", lastname="Doe"):
    if not (isinstance(firstname, str) and isinstance(lastname, str)):
        raise TypeError("Les paramètres doivent être des chaînes")
    return f"Hello, {firstname} {lastname}!"
