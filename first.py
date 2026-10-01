
def sude_nebo_liche(cislo):
    if cislo%2==0:
        print(f"Cislo {cislo} je sude")
    if cislo%2==1:
        print(f"Cislo {cislo} je liche")
    else:
        print("nezadal jsi cislo ale " cislo)


if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
    sude_nebo_liche(23)
    sude_nebo_liche(ahoj)