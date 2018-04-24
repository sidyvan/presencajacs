from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.models import Aluno, Presenca
from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum
from datetime import datetime


def home(request):

    q = request.GET.get('q', '')

    alunos_lista = Presenca.objects.filter(
        Q(ra__contains=q) 
       
        ).values('nome','ra').distinct()
    paginator = Paginator(alunos_lista, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos = paginator.page(1)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)

    context = {
        'alunos':alunos,

    }
    return render(request, 'secretaria/home.html', context)




def detalhe(request, ra):

    lista = Presenca.objects.filter(ra=ra)
    aluno = get_object_or_404(Aluno, ra=ra)

    #soma = Presenca.objects.filter(ra=ra).values('tempo').annotate(Sum('tempo'))
    soma = '00:00:00'
    f = '%H:%M:%S'
    soma =  datetime.strptime(soma, f).time()
    
    for l in lista:
        #soma = soma + l.tempo
        soma = l.tempo

      


    

    context = {
        'lista':lista, 
        'aluno':aluno,  
        'soma':soma,    
    }
    return render(request, 'secretaria/detalhe.html', context)





'''
def login_admin(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #lista = Aluno.objects.all()
                    #quantidade = Aluno.objects.count()
                    return HttpResponseRedirect('/painel')
                else:
                    return render(request, 'painel/login.html', {'form':form})
            else:
                return render(request, 'painel/login.html', {'form':form})
        else:
            return render(request, 'painel/login.html', {'form':form})
    else:
        return render(request, 'painel/login.html', {'form':form})
'''