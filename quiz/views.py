from django.shortcuts import render

def start(request):
	return render(request, "quiz/start.html")
def quiz(request):
	return render(request, "quiz/quiz.html")
def question(request):
	return render(request, "quiz/question.html")
def results(request):
	return render(request, "quiz/results.html")