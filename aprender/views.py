from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotAllowed

from .models import Quiz, Question

import random

def home(request):
    return render(request, "home.html")

def tense(request,id = ""):
	if id == "":
		return render(request, "tenses/tenseHome" + id +".html")
	return render(request, "tenses/" + id +".html")

def vocab(request,id = ""):
	if id == "":
		return render(request, "vocab/vocabHome" + id +".html")
	return render(request, "vocab/" + id +".html")

def grammar(request,id = ""):
	if id == "":
		return render(request, "grammar/grammarHome" + id +".html")
	return render(request, "grammar/" + id +".html")

def update_session(request):
	if not request.method=='POST':
		return HttpResponseNotAllowed(['POST'])
	request.session['prevQues'] = request.session.get('curQues',None)
	request.session['curQues'] = None
	return HttpResponse('ok')

def getNewQuestion(quiz,request):
	numQuestions = len(quiz.questions.all())
	ind = random.randint(0,numQuestions-1)
	print(ind)
	while(quiz.questions.all()[ind].id == request.session.get('prevQues',None) and numQuestions>1):
		ind = random.randint(0,numQuestions-1)
	return quiz.questions.all()[ind]

def practice(request,id = ""):
	if id == "":
		return render(request, "practice/practiceHome" + id +".html")
	try:
		quiz = Quiz.objects.get(name__iexact=id)
		#curQues = request.session.get('my_car', 'mini')
		#tries = request.session.get('my_car', 'mini')

	except:
		raise Http404("Quiz does not exist")
	#print(quiz.questions.all())
	if len(quiz.questions.all()) == 0:
		raise Http404("Quiz has no questions")

	if quiz.questions.filter(id=request.session.get('curQues',None)).exists():
		question = quiz.questions.get(pk=request.session.get('curQues',None))
	else:
		question = getNewQuestion(quiz,request)

	request.session['curQues'] = question.id

	choices = {}

	if question.choice1 != "":
		choices[1] = question.choice1
	if question.choice2 != "":
		choices[2] = question.choice2
	if question.choice3 != "":
		choices[3] = question.choice3 
	if question.choice4 != "":
		choices[4] = question.choice4
	keys =  list(choices.keys())
	random.shuffle(keys)

	randChoices = {}
	for key in keys:
		randChoices.update({key:choices[key]})
	return render(request, "practice/quizForm.html",{'title':quiz.displayName,'question':question,'choices':randChoices})

#def vocab(request):
#	return render(request, "vocab/vocabHome.html")
def help(request):
	return render(request, "help.html")