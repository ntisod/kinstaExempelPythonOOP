import cafe, oopcafe

val = input("Välj 1 för funktionellt programmerat café. Välj 2 för objektorienterat programmerat café. Välj 0 för att avsluta. Vad vill du göra:")

while val!="0":
  
  if(val=="1"):
    cafe.FunctionalCafe()
  elif(val=="2"):
    oopcafe.OopCafe()
  elif(val=="0"):
    exit

  val = input("Välj 1 för funktionellt programmerat café. Välj 2 för objektorienterat programmerat café. Välj 0 för att avsluta. Vad vill du göra:")
