import easygui
a=easygui.choicebox("enter the choice","choices",["encryption","decryption"])
if a=="encryption":
	print "you have selected encryption"
if a=="decryption":
	print "you have selected decryption"
