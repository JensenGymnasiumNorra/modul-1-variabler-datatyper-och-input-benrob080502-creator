"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""
namn = input("vad heter du? ")
ålder= int(input("hur gammal är du? "))

pension = 67

årkvar = (pension-ålder)

print(f"Hej {namn} du har {årkvar} tills du går i pension")