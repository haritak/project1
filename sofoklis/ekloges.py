math = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
times=1
leuko=0
akiro=0

while True:
	print "\nDose noumero pou na exei stauro, 'T' gia telos, 'L' gia leuko, 'A' gia akiro"
	x=raw_input(": ")
	if x=='TELEIOSAME':
            for i in range(0, len(math) ):
		print "Mathitis ",i,": ",math[i],"Stavrous"
            print "\nLeuko: ",leuko
            print "\nAkiro: ",akiro
            print "\nSofoklis Fasoulakis 10/10/2017 Thanks for your preference!"
            break
	elif x=='T':
		times+=1
		print "\nTelos Psifodeltiou"
		print "\n",times,"o PSIFODELTIO:"
	elif x=='L':
		leuko+=1
		print "\nLeuko"
	elif x=='A':
		akiro+=1
		print "\nAkiro"
	else:
            x = int(x)
            math[x] += 1
            print "Mathitis ",x
		
		
		
