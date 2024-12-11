def mafct(a, b=5):
    return a+b


x = 3
print(mafct(x, 3))
print(mafct(x))

def ajouter_elt(lst = [0,1,2], elt = 3):
    lst.append(elt)
    return lst

print(ajouter_elt())

def ajouter_carac(ch = "abc", elt = "d"):
    ch += elt
    return ch

print(ajouter_carac())