from django.shortcuts import render
from django.http import HttpResponse

from .models import M1Question



def index(request):

    m1questions = M1Question.objects.all()
    context = {'m1questions':m1questions}
    return render(request, 'elections/index.html', context)

def M1QDs(request, M1QD):
    return HttpResponse(M1QD)

def vote(request):

    m1questions = M1Question.objects.all()



    selected_choice = request.POST['choice']

    if selected_choice == "One":
        M1Question.One = True

    elif selected_choice == "Two":
        M1Question.Two = True

    elif selected_choice == "Three":
        M1Question.Three = True

    elif selected_choice == "Four":
        M1Question.Four = True

    elif selected_choice == "Five":
        M1Question.Four = True





    return HttpResponse(M1Question.Three)