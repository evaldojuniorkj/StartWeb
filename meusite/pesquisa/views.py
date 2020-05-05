from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Questao, Escolha
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    ultimas_questoes = Questao.objects.order_by('-data_publicacao')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'ultimas_questoes': ultimas_questoes
    }
    return render(request, 'polls/index.html', context)


def detalhe(request, questao_id):
    try:
        questao = Questao.objects.get(pk=questao_id)
    except Questao.DoesNotExist:
        raise Http404('Questao nao existe!')
    return render(request, 'polls/detalhe.html', {'questao': questao})


def resultado(request, questao_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % questao_id)


def votacao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        escolha_selecionada = questao.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        return render(request, 'polls/detalhe.html', {
            'questao': questao,
            'error_message': "Você não selecionou uma escolha.",
        })
    else:
        escolha_selecionada.votos += 1
        escolha_selecionada.save()
        print(questao_id)
        return HttpResponseRedirect(reverse('polls:resultado', args=[questao_id]))

def resultado(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'polls/resultado.html', {'questao': questao})