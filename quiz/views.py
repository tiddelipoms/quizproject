from quiz.models import Quiz
from django.shortcuts import render
from django.shortcuts import redirect

def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[int(question_number) - 1]
	context = {
		"question_number": question_number,
		"question": question.question,
		"question_image": question.question_image,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"quiz": quiz,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def answer(request, quiz_number, question_number):
	saved_answers = request.session.get(quiz_number, {})
	answer = int(request.POST["answer"])
	saved_answers[question_number] = answer
	request.session[quiz_number] = saved_answers
	question_number = int(question_number)
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	num_questions = quiz.questions.count()
	if num_questions <= question_number:
		return redirect("results_page", quiz_number)
	else:
		return redirect("question_page", quiz_number, question_number + 1)

def results(request, quiz_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = list(quiz.questions.all())
	saved_answers = request.session.get(quiz_number, {})
	num_correct_answer = 0
	for question_number, answer in saved_answers.items():
		correct_answer = questions[int(question_number) - 1].correct
		if correct_answer == answer:
			num_correct_answer += 1
		questions[int(question_number) - 1].user_answer = answer
	context= {
		"correct": num_correct_answer,
		"total": len(questions),
		"questions": questions,
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)