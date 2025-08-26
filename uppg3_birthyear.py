"""  
Skapa en variabel för ditt födelseår
Programmet ska sedan skriva ut din ålder

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Du är (16) år gammal.

"""

from datetime import datetime

fodelsear = int(input("vilket år är du född? "))

nurvarande_ar = datetime.now().year

alder = nurvarande_ar - fodelsear

print(f"du är ungerfär {alder} år gammal.")