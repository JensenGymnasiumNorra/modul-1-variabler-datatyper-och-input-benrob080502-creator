"""  
Låt användaren skriva in ett valfritt tal. Skriv sedan ut vad det talet blir i kvadrat:

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
(3) i kvadrat är (9). 

"""

nummer1 = int(input("säg ett nummer max upp till 10: "))
upphöjt = int(input("säg ett nummer som du vill upphöja med: "))

totalt = (nummer1**upphöjt)

print(f"totalt blir det {totalt} ")
