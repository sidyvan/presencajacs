from datetime import datetime
import time


def calcula(entrada, saida):
	
	s =   ('{:%Y-%m-%d %H:%M:%S}'.format(entrada))
	t =  ('{:%Y-%m-%d %H:%M:%S}'.format(saida))
	f = '%Y-%m-%d %H:%M:%S'
	
	dif = ((datetime.strptime(t, f) - datetime.strptime(s, f))).total_seconds() 

	tempo = time.strftime("%H:%M:%S", time.gmtime(dif))
	return tempo  

