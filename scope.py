#Scope y alcance:



def create_name(text):
    name = text;
    return f"tu nombre es {name}"

def create_lastname(text):
    lastname = text;
    return f"tu apellido es {lastname}"

def what_is_your_name():
    name = input("¿Me dirias tu nombre? y yo lo aprendere: ")
    return name

def what_is_your_lastname():
    lastname = input("¿Me dirias tu apellido? y yo lo aprendere: ")
    return lastname

def create_fullname():
    name = what_is_your_name()
    lastname = what_is_your_lastname()
    my_name_is = create_name(name)
    my_lastname_is = create_lastname(lastname)

    print(my_name_is + " y " + my_lastname_is)


create_fullname()