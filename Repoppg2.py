def meny():
    #valg om hva man vil gjøre
    print("Velg et valg:")
    print("1: Registrer deltaker")
    print("2: List ut deltakere")
    print("3: Registrer tid på deltaker")
    print("0: Avslutt")
    #gjør om valg til int.
    valg = int(input("Valg: "))
    #returner valg
    return valg

def registrerDeltaker():
    print("Registrer deltaker")
    #spør om fornavn, etternavn, deltakernummer og deltaker.
    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn: ")
    deltakernummer = input("Deltakerens nummer: ")
    deltaker = {"fornavn":fornavn, "etternavn":etternavn, "nr":deltakernummer, "tid":0}
    #returnern deltaker variablen.
    return deltaker

def listUtDeltakere(deltakere):
    print("Lister ut deltakere")
    #for alle singulere deltakere i deltakere
    for deltaker in deltakere:
        #print ut informasjon om deltaker fra dict.
        print("")
        print(f'Deltakernummer: {deltaker["nr"]}')
        print(f'fornavn: {deltaker["fornavn"]}')
        print("Etternavn: " + deltaker["etternavn"])
        print(f"Tid: {deltaker['tid']}")

def registrerTid():
    #ikke utviklet.
    print("Registrering av tid")
    print("Funksjonen er ikke utviklet :) ")
    return


def main():
    #deltakerer dictionary
    deltakere = []
    while True:
        print("Program Løpetider.")
        print("")
        valg = meny()
        if valg == 0:
            break
        elif valg == 1:
            #gå gjennom registrering, deretter 
            deltaker = registrerDeltaker()
            deltakere.append(deltaker)
        elif valg == 2:
            #list ut deltakere.
            listUtDeltakere(deltakere)
        elif valg == 3:
            #registrer tid
            registrerTid()
        else:
            #feilmelding
            print("Menyvalget finnes ikke")

main()