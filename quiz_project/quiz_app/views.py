from django.shortcuts import render, redirect
from .models import Question

def start_quiz(request):
    request.session['score'] = 0
    request.session['answers'] = {}
    return redirect('quiz_question', q_no=1)

def quiz_question(request, q_no):
    questions = list(Question.objects.all())
    total_questions = len(questions)

    if q_no > total_questions:
        return redirect('quiz_result')

    question = questions[q_no - 1]

    if request.method == 'POST':
        selected = request.POST.get('answer')
        if selected == question.correct_answer:
            request.session['score'] += 1
        request.session['answers'][str(question.id)] = selected
        return redirect('quiz_question', q_no=q_no + 1)

    return render(request, 'quiz_app/question.html', {
        'question': question,
        'q_no': q_no,
        'total': total_questions
    })

def quiz_result(request):
    return render(request, 'quiz_app/result.html', {
        'score': request.session.get('score', 0),
        'total': Question.objects.count()
    })

