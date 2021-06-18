from spillebrett import Spillebrett #importerer Spillbrett fra spillbrett

#Målet med dette programmet er å lage conways game of life.
#Ved hjelp av klassene Celler og Spillbrett.

def main(): #Hovedprogram
    antallRader = int(input("Hvor mange rader skal spillebrettet ha? ")) #Bruker skriver inn input for hvor mange rader spillbrettet skal ha
    antallKolonner = int(input("Hvor mange kolonner skal spillbrettet ha? ")) #Bruker skriver inn input for hvor mange kolonner spillbnrettet skal ha
    E1 = Spillebrett(antallRader, antallKolonner) #Spillbrettet blir opprettet

    svar = None #Svar starter som "None" for å sette i gang while løkken
    while svar != "q": #Sålenge brukeren oppdaterer svar variabelet til å være alt annet enn q vil loopen fortsette
        print("\n"*100) #Blank space (gjør at det ser bedre ut)
        E1.tegnBrett() #Tegner brettet ved bruk av en metode fra Spillbrett
        print("\n", "Generasjon:", E1.oppdatering(),"-","Antall levende:",E1.finnAntallLevende()) #Oppdaterer spillbrettet, og skriver ut generasjonsnummer og antall levende
        svar = input("\nTast [ enter ] for a fortsette, eller [ q ] for a avslutte\n: ").lower() #Brukeren skriver inn input, alt annet enn q vil få loopen til å fortsette
main() #hovedprogrammet kjøres.
