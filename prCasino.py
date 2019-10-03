#-*- coding: utf8 -*-
import os
import random
import math

cagnotte = 1000

reponse = "o"


while reponse == "o":
	
	print ("votre cagnotte est de :", cagnotte,"$")
	tirage = random.randrange(49)
	print ("le n° tiré est le",tirage,"mais il faut pas le dire, c'est de la triche pour mon titou! ")

	gain = 0
	user_mise = 0

#déclaration mise sur un n° entre 0 et 49
	user_number = int(input("chosissez un nombre entre 0 et 49"))
	
	while user_number < 0 or user_number > 49:
		user_number = int(input("on vous à dit entre 0 et 49 !!!"))
#déclaraion mise argent
	user_mise = int(input("quel montant voulez vous miser ?"))
	while user_mise > cagnotte:
		user_mise = int(input("vous avez miser trop !!!"))
		
	cagnotte = cagnotte - user_mise
	
	if user_number == tirage:
		gain = user_mise * 3
		print ("VOUS AVEZ GAGNE : ", gain,"$, votre cagnotte est de :",cagnotte + user_mise + gain,"$" )
		cagnotte = cagnotte + user_mise + gain
		reponse = input("voulez_vous continuer ?")
	elif tirage % 2 == 0 and user_number % 2 == 0:
		gain = user_mise + (user_mise / 2)
		gain = math.ceil(gain) #essai ceil
		cagnotte = cagnotte + user_mise + gain
		print ("vous avez gagné la couleur pair",  gain,"$ votre cagnotte est de :", cagnotte,"$" )
		reponse = input("voulez_vous continuer ?")
		reponse.lower()
	elif tirage % 2 == 1 and user_number % 2 == 1:
		gain = user_mise + (user_mise / 2)
		gain = math.ceil(gain) #essai ceil
		print ("vous avez gagné la couleur impair", gain, "votre cagnotte est de", cagnotte,"$" )
		cagnotte = cagnotte + user_mise + gain
		reponse = input("voulez_vous continuer ?")
		reponse.lower()
	else:
		cagnotte = cagnotte - user_mise
		print ("vous avez perdu ! votre cagnotte est de : ", cagnotte,"$")
		reponse = input("voulez_vous continuer ?")
		reponse.lower()

if cagnotte < 1:
		print ("vous n'avez plus d'argent ! a bientôt")
		reponse = "n"




os.system("pause")
