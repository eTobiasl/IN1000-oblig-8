class Celle:

#Målet med dette programmet er å opprette en klasse som lar brukeren
#oprette celler, og metoder som lar brukeren sjekke og endre statusen på cellene.
#klassen skal også ha en metode som lar brukeren hente cellens status tegn.

    def __init__(self): #konstruktøren
        self._status = "dod" #statusen starter som død

    def settDoed(self): #Metode for å sette statusen til en celle til død
        self._status = "dod"

    def settLevende(self): #Metode for å sette statusen til en celle til levende
        self._status = "levende"

    def erLevende(self): #Sjekker om cellen er levende
        if self._status == "levende": #Hvis cellen er levende
            return True
        else: #Hvis den ikke er levende
            return False

    def hentStatusTegn(self):
        if self.erLevende(): #Hvis den er levende
            return "O" #returneres dette
        else: #Hvis den ikke er levende
            return "." #returneres dette
