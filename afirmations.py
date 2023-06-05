"""Programación defensiva"""

def evaluate_letter(letter_list):
    first_letter = []

    for letter in letter_list:
        assert type(letter) == str, f"Palabra no es str"
        assert len(letter) > 0, "No se permiten str vacios"
        first_letter.append(letter[0])

    print(first_letter[0])
    return first_letter

#Enviamos una tupla
evaluate_letter({"":""})
# evaluate_letter({"Prueba":"Prueba"})