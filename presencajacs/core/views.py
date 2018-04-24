from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from core.models import Presenca, Aluno
from core.forms import PresencaForm
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core import calculatempo




def calcula_tempo(request):

	lista_tempo_vazio = Presenca.objects.filter(tempo=None)

	for l in lista_tempo_vazio:

		obj = get_object_or_404(Presenca, pk=l.pk)
		entrada = obj.data_hora_entrada
		saida = obj.data_hora_saida
		l.tempo = calculatempo.calcula(entrada, saida)
		l.save()

	#return render(request, 'core/index.html', {})
	return redirect('entrada')


def index(request):
	total_entrada = Presenca.objects.all().values('ra').distinct()
	return render(request, 'core/index.html', {

		'total_entrada':total_entrada

	 })


def entrada(request):

	lista_aux = Presenca.objects.filter(data_hora_saida__isnull=False).order_by('-data_hora_saida')
	
	form = PresencaForm(request.POST or None)
	tempo = ''

	lista_dentro = Presenca.objects.filter(data_hora_saida=None).order_by('-data_hora_entrada')
	if request.method == 'POST':

		ra = request.POST['ra']

		lista_presenca = Presenca.objects.filter(ra=ra).order_by('-pk')[:1]
		
		lista_presenca_count = Presenca.objects.filter(ra=ra,data_hora_saida=None).order_by('-data_hora_saida').count()

		if lista_presenca_count == 0:
	
			if form.is_valid():
				salvar = form.save(commit=False)

				if Aluno.objects.filter(ra=ra).exists():
					aluno = get_object_or_404(Aluno, ra=ra)
					salvar.nome = aluno.nome
					salvar.fase = aluno.fase
					salvar.email = aluno.email
				else:
					salvar.nome = 'Sem nome'
				



				salvar.save()
		else:
			presenca_obj = get_object_or_404(Presenca, pk=lista_presenca)

			presenca_obj.data_hora_saida = datetime.now()
			#tempo = presenca_obj.data_hora_saida - lista_presenca.data_hora_entrada

			#entrada = presenca_obj.data_hora_entrada
			#saida = presenca_obj.data_hora_saida

			entrada = presenca_obj.data_hora_entrada
			
			saida = presenca_obj.data_hora_saida

			t = calculatempo.calcula(entrada, saida)

			presenca_obj.tempo = t
			presenca_obj.save()


	paginator = Paginator(lista_aux, 25) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		lista = paginator.page(1)
	except EmptyPage:
		lista = paginator.page(paginator.num_pages)


	return render(request, 'core/entrada.html',{
		'lista':lista,
		'form':form,
		'tempo':tempo,
		'lista_dentro':lista_dentro,
	
		})
	

def saida_coletiva(request):
	date_hora = ''
	lista_dentro = Presenca.objects.filter(data_hora_saida=None).order_by('-data_hora_entrada')
	if request.method == 'POST':

		date_hora = request.POST['datahora']

		for l in lista_dentro:


			l.data_hora_saida = date_hora

			l.save()

		return redirect('calcula_tempo')
		lista_dentro = Presenca.objects.filter(data_hora_saida=None).order_by('-data_hora_entrada')

		#lista_update = Presenca.objects.filter(data_hora_saida=None).update(data_hora_saida=date_hora)


	return render(request, 'core/saida_coletiva.html',{
		'date_hora':date_hora,
		'lista_dentro':lista_dentro

		})