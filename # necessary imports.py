# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars


def utvalg():
    print("""
    1. generer passord med alt aktivert.
    2. generer passord med bare bokstaver og tall
    3. generer passord med bokstaver og spesielle bokstaver
    4. generer passord med bare bokstaver
    5. avslutt""")

def main():
    run = True
    while run:
        utvalg()

        valg = input(": ")

        if valg == "1":
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation

            alphabet = letters + digits + special_chars
        elif valg == "2":
            letters = string.ascii_letters
            digits = string.digits

            alphabet = letters + digits 
        elif valg == "3":
            letters = string.ascii_letters
            special_chars = string.punctuation

            alphabet = letters + special_chars
        elif valg == "4":
            letters = string.ascii_letters

            alphabet = letters + special_chars
        elif valg == "5":
            run = False
            quit()
        passordlengde = input("Skriv in lengsde på passord: ")
        if passordlengde.isdigit():
            try:

                passordlengde = int(passordlengde)
                # generate a password string
                pwd = ''
                for i in range(passordlengde):
                    pwd += ''.join(secrets.choice(alphabet))

                print(pwd)
            except SyntaxError as e:
                print("Feilmelding")
                print(e)
        else:
            print("Ikke gyldig verdi.")

main()