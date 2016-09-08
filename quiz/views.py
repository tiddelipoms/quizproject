from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
		"name": "Klassiska böcker",
		"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
		"name": "Största 1slagen",
		"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
		"name": "Världens mest kända hackare",
		"decription": "Hackerhistoria är viktigt, kan du den?"
	},
]

def start(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) -1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)
def question(request):
	return render(request, "quiz/question.html")
def results(request):
	return render(request, "quiz/results.html")