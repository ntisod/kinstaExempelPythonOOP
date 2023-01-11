def FunctionalCafe():
  small = 2
  regular = 5
  big = 6
   
  user_budget = input('Hur mycket pengar kan du använda? ')
   
  try:
     user_budget = int(user_budget)
  except:
     print('Skriv ett numeriskt värde!')
     exit()
   
  if user_budget > 0:
     if user_budget >= big:
         print('Du har råd med en stor kaffe.')
         if user_budget == big:
             print('Det är precis.')
         else:
             print('Din växel blir ', user_budget - big)
     elif user_budget == regular:
         print('Du har råd med en normal kaffe.')
         print('Det är precis.')
     elif user_budget >= small:
         print('Du har råd med en normal kaffe.')
         if user_budget == small:
             print('Det är precis.')
         else:
             print('Din växel blir ', user_budget - small)
  