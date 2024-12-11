def nettoyer_texte(texte):
    import unicodedata
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if c.isalpha())  # Garder seulement les lettres
    return texte.lower()

def est_palindrome(chaine):
    chaine_epuree = nettoyer_texte(chaine)
    return chaine_epuree == chaine_epuree[::-1]

phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
