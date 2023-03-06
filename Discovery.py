import os
import requests
from termcolor import colored

prompt = "\.:°Discovery]°:./\__-> "

def getReponse(url_complet):
	try:
		return requests.get("http://"+url_complet)
	except requests.exceptions.ConnectionError:
		pass

def main():
	os.system("clear")
	print(colored(banner,"yellow","on_red"))
	print(colored(title, "white","on_red",attrs=["blink", "bold"]))

	print(colored("[1] Chercher des dossiers cachés dans le serveur web","magenta"))
	print(colored("[2] Chercher des sous domaines du site web\n","magenta"))
	choix = int(input(colored("Votre choix ? ","yellow")))

	if choix != 1 and choix != 2:
		print(colored("[ERREUR] Veuillez entrer 1 ou 2 ! Quittons le programme...","red",attrs=["bold"]))
		quit()

	print("\n")
	url = input(colored(prompt+"Entrez l'URL à bruteforce: ","yellow"))

	if choix == 1:
		nom_fichier = input(colored(prompt+"Entrez le nom du fichier contenant les dossiers à bruteforce: ","yellow"))
		fichier = open(nom_fichier,"r")

		print("\n")
		for ligne in fichier:
			mot = ligne.strip()
			url_complet = url+"/"+mot
			reponse = getReponse(url_complet)
			#Si on a une réponse. (Si ça à fonctionné)
			if reponse:
				print(colored(prompt+"URL Découverte ! "+url_complet,"green",attrs=["bold"]))
	else:
		nom_fichier = input(colored(prompt+"Entrez le nom du fichier contenant les sous domaines à bruteforce: ","yellow"))
		fichier = open(nom_fichier,"r")

		print("\n")
		for ligne in fichier:
			mot = ligne.strip()
			url_complet = mot+"."+url
			reponse = getReponse(url_complet)
			#Si on a une réponse. (Si ça à fonctionné)
			if reponse:
				print(colored(prompt+"SOUS DOMAINE Découvert ! "+url_complet,"green",attrs=["bold"]))

		print("\n\n")

banner=("                                                    \n"+
"  ·▄▄▄▄  ▪  .▄▄ ·  ▄▄·        ▌ ▐·▄▄▄ .▄▄▄   ▄· ▄▌  \n"+
"  ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▪█·█▌▀▄.▀·▀▄ █·▐█▪██▌  \n"+
"  ▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ ▐█▌▐█▪  \n"+
"  ██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌ ▐█▀·.  \n"+
"  ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀  ▀ •   \n"+
"                                                    \n"+
"                                                    ")

title=("    Secret Website Data Finder by b64-Sm9yZGFuIExBSVJFUw     \n"+
"                                                    \n\n")

main()
