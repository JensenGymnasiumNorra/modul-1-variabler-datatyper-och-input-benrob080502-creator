"""  
Skapa en variabel för ditt namn.
Skapa en variabel för din ålder.
Skriv ut ditt namn med hjälp av variabeln.

Skapa en variabel och låt användaren skriva in sitt namn med hjälp av input.
Skapa en variabel och låt användaren skriva in sin ålder med hjälp av input.

Skriv ut en mening som använder sig av alla 4 variabler. Åldern ska adderas ihop.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Välkommen till mitt program (Oskar). Du och (Hampus) är (53) år tillsammans.

"""

namn1 = input("vad heter du? ")
namn2 = input("vad heter du? ")

ålder1 = int(input("hur gammal är du ? "))
ålder2 = int(input("hur gammal är du ? "))

totalt = (ålder1+ålder2)

print(f"välkomen både {namn1} och {namn2} till vår hemsida tillsammans är ni {totalt} år gammla!  ")