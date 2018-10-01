# hangman.py
def display_platform(wrong_guesses):
  if len(wrong_guesses)==0:
    print(' _____'+'\n'+' |'+'\n'+' |'+'\n'+' |'+'\n'+'_|__')
  elif len(wrong_guesses)==1:
    print(' _____'+'\n'+' |  Ó'+'\n'+' |'+'\n'+' |'+'\n'+'_|__')
  elif len(wrong_guesses)==2:
    print(' _____'+'\n'+' |  Ó'+'\n'+' |  |'+'\n'+' |'+'\n'+'_|__')
  elif len(wrong_guesses)==3:
    print(' _____'+'\n'+' |  Ó'+'\n'+' | /|'+'\n'+' |'+'\n'+'_|__')
  elif len(wrong_guesses)==4:
    print(' _____'+'\n'+' |  Ó'+'\n'+' | /|\ '+'\n'+' |'+'\n'+'_|__')
  elif len(wrong_guesses)==5:
    print(' _____'+'\n'+' |  Ó'+'\n'+' | /|\ '+'\n'+' | /'+'\n'+'_|__')
  else:
    print(' _____'+'\n'+' |  Ó'+'\n'+' | /|\ '+'\n'+' | / \ '+'\n'+'_|__')
#assert display_platform('s')==print(' _____'+'\n'+' |  Ó'+'\n'+' |'+'\n'+' |'+'\n'+'_|__')
#assert display_platform('uhe') ==print (' _____'+'\n'+' |  Ó'+'\n'+' | /|'+'\n'+' |'+'\n'+'_|__')
#assert display_platform('ijufxb) ==print (' _____'+'\n'+' |  Ó'+'\n'+' | /|\ '+'\n'+' | / \ '+'\n'+'_|__')
