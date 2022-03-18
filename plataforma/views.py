from multiprocessing import context
from operator import concat, mod
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Veiculo, Contato


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    
    if preco_minimo or preco_maximo:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999

        veiculos = Veiculo.objects.filter(valor__gte=preco_minimo)\
                                                    .filter(valor__lte=preco_maximo)
    else:
        veiculos = Veiculo.objects.all()
    
    return render(request, 'home.html', {'veiculos': veiculos})

def sobre(request):
    return render(request,'sobre.html')

def veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    imagens = []
    imagens.append(veiculo.imagem1.url)
    imagens.append(veiculo.imagem2.url)
    imagens.append(veiculo.imagem3.url)
    sugestoes = Veiculo.objects.filter(cidade=veiculo.cidade).exclude(id=id)[:2]
    return render(request, 'veiculo.html', {'veiculo': veiculo, 'sugestoes': sugestoes, 'id': id, 'imagens': imagens,})


def anuncie(request):
    if request.method=="GET":
        return render(request, 'anuncie.html',)
    else:
        contact = Veiculo()
        modelo = request.POST.get('modelo')
        valor = request.POST.get('valor')
        kmRodados = request.POST.get('kmRodados')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        tipo_combustivel = request.POST.get('tipo_combustivel')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        descricao = request.POST.get('descricao')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        imagem1 = request.FILES.get('img1')
        imagem2 = request.FILES.get('img2')
        imagem3 = request.FILES.get('img3')
        
        contact.modelo = modelo
        contact.valor = valor
        contact.kmRodados = kmRodados
        contact.ano = ano
        contact.cor = cor
        contact.tipo_combustivel = tipo_combustivel
        contact.cidade = cidade
        contact.telefone = telefone
        contact.descricao= descricao
        contact.bairro = bairro
        contact.rua = rua
        contact.imagem1 = imagem1
        contact.imagem2 = imagem2
        contact.imagem3 = imagem3
    try:
        contact.save()
        return redirect('home')
    except:
        return render(request,'anuncie.html',)

def pesquisar(request):
    pesquisa = request.POST.get('pesquisa')
    if Veiculo.objects.filter(modelo__icontains=pesquisa,):
        veiculos = Veiculo.objects.filter(modelo__icontains=pesquisa,)
    elif Veiculo.objects.filter(cor__icontains=pesquisa,):
        veiculos = Veiculo.objects.filter(cor__icontains=pesquisa,)
    elif Veiculo.objects.filter(cidade__icontains=pesquisa,):
        veiculos = Veiculo.objects.filter(cidade__icontains=pesquisa,)
    else:
        veiculos = Veiculo.objects.all()
    return render(request, 'home.html', {'veiculos': veiculos})


def contato(request):
    if request.method=="GET":
        return render(request, 'contato.html')
    else:
        contact = Contato()
        name = request.POST.get('name')
        email = request.POST.get('emailC')
        telefone = request.POST.get('telefone')
        subject = request.POST.get('mensagem')
        contact.name = name
        contact.email = email
        contact.telefone = telefone
        contact.mensagem = subject
        contact.save()
        return render(request,'contato.html')