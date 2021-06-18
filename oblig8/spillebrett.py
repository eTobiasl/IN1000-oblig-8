from random import randint #Importerer randint fra random
from celle import Celle #Importerer Celle fra celle

#Målet med dette programmet er å oprette en klasse som lar deg skape et spillebrett,
#med metoder som gjør at man kan lage conways game of life

class Spillebrett:
    def __init__(self, rader, kolonner): #Konstruktør
        self._rader = rader #Instansvariabel for antall rader
        self._kolonner = kolonner #Instansvariabel for antall kolonner
        self._generasjonsnummer = -1 #Instansvariabel for generasjonsnummeret
        self._rutenett = [] #Instansvariabel som holder rutenettet
        for r in range(0, rader): #Lager rutenettet
            self._rutenett.append([]) 
            for k in range(0, kolonner): 
                self._rutenett[r].append(Celle())
        self._generer() #Bruker metoden _generer


    def tegnBrett(self):
        for i in range(0,len(self._rutenett)):
            for r in self._rutenett[i]:
                print(r.hentStatusTegn(),end="")
            print()
# printer ut rutenettet ved bruk av  metoden hentStatusTegn()

    def oppdatering(self):
        self._generasjonsnummer += 1 #plusser på generasjonsnummret for hver iterasjon
        levendeDod = [] #Liste som holder alle levende celler som skal dø
        dodLevende = [] #Liste som holder alle døde celler som skal bli levende
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                levendeNaboer = 0
                naboer = self.finnNabo(rad, kolonne)
                for n in naboer: #itererer gjennom nabo celler
                    if n.erLevende(): #sjekker om cellen er levende
                        levendeNaboer += 1 #for hver levende celle legges 1 til for å lage en teller av levende naboer
                if self._rutenett[rad][kolonne].erLevende(): #sjekker om cellen er levende
                    if levendeNaboer < 2 or levendeNaboer > 3:
                        levendeDod.append(self._rutenett[rad][kolonne])
                else: #Hvis cellen ikke er levende
                    if levendeNaboer == 3:
                        dodLevende.append(self._rutenett[rad][kolonne])
        for i in dodLevende:
            i.settLevende() #Setter status til levende
        for j in levendeDod:
            j.settDoed() #Setter status til død
            #Går gjennom listene og endrer statusene til cellene ved hjekp av 2 for-løkker.
        return self._generasjonsnummer #returnerer hvilken generasjon rutenettet er i

    def finnAntallLevende(self): # Går gjennom rutenettet for å finne hvor mange levende celler det har.
        levende = 0
        for i in self._rutenett:
            for j in i:
                if j.erLevende(): #sjekker status på cellen
                    levende += 1 #levende variabelen blir plusset på 1 for hver levende celle
        return levende #returnerer antall levende celler

    def _generer(self): #Lager "seed". velger hvilke celler som skal være døde og levende.
        for i in self._rutenett:
            for j in i:
                if randint(1,3) == 1: # 1/3 av cellene
                    j.settLevende() #får status levende
                else: #resten
                    j.settDoed() #får status død

    def finnNabo(self, rad, kolonne): #Finner naboene til cellen
        naboCeller = [] #Liste hvor nabocellene blir lagt til etterpå
        for i in range(self._rader):
            for j in range(self._kolonner):
                if 0 <= i < self._rader and 0 <= i < self._kolonner: #eliminerer alle cellene utenfor rutenettet
                    if i == rad: #Legger til de nabocellene på samme rad som cellen
                        if j == kolonne + 1 or j == kolonne -1:
                            naboCeller.append(self._rutenett[i][j])
                    if i == rad + 1: #Legger til nabocellene til raden etter cellen
                        if j == kolonne + 1 or j == kolonne or j == kolonne -1:
                            naboCeller.append(self._rutenett[i][j])
                    if i == rad -1: #Legger til nabocellene til raden før cellen
                        if j == kolonne + 1 or j == kolonne or j == kolonne -1:
                            naboCeller.append(self._rutenett[i][j])
        return naboCeller #returnerer listen over naboceller
