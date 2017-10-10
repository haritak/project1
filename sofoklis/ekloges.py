mathA=0
mathB=0
mathC=0
mathD=0
mathE=0
mathF=0
mathG=0
mathH=0
mathI=0
mathK=0
times=1
leuko=0
akiro=0

while True:
	print "\nDose noumero pou na exei stauro, 'T' gia telos, 'L' gia leuko, 'A' gia akiro"
	x=raw_input(": ")
	if x=='TELEIOSAME':
		print "\nMathitis 1: ",mathA,"Stavrous"
		print "\nMathitis 2: ",mathB,"Stavrous"
		print "\nMathitis 3: ",mathC,"Stavrous"
		print "\nMathitis 4: ",mathD,"Stavrous"
		print "\nMathitis 5: ",mathE,"Stavrous"
		print "\nMathitis 6: ",mathF,"Stavrous"
		print "\nMathitis 7: ",mathG,"Stavrous"
		print "\nMathitis 8: ",mathH,"Stavrous"
		print "\nMathitis 9: ",mathI,"Stavrous"
		print "\nMathitis 10: ",mathK,"Stavrous"
		print "\nLeuko: ",leuko
		print "\nAkiro: ",akiro
		print "\nSofoklis Fasoulakis 10/10/2017 Thanks for your preference!"
		break
	elif x=='1':
		mathA+=1
		print "\nMathitis1"
	elif x=='2':
		mathB+=1
		print "\nMathitis2"
	elif x=='3':
		mathC+=1
		print "\nMathitis3"
	elif x=='4':
		mathD+=1
		print "\nMathitis4"
	elif x=='5':
		mathE+=1
		print "\nMathitis5"
	elif x=='6':
		mathF+=1
		print "\nMathitis6"
	elif x=='7':
		mathG+=1
		print "\nMathitis7"
	elif x=='8':
		mathH+=1
		print "\nMathitis8"
	elif x=='9':
		mathI+=1
		print "\nMathitis9"
	elif x=='10':
		mathK+=1
		print "\nMathitis10"
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
		print "\nKati ekanes lathos!"
		continue
	
		
		
		
