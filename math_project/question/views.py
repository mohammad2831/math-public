from django.shortcuts import render
from django.views import View
from .models import Question,Stage


from django.shortcuts import render, get_object_or_404, redirect


class AllQuestionView(View):
    def get(self, request):
        question = Question.all()
        

class QuestionView(View):
    def get(self, request, id_q, id_s):
        question = get_object_or_404(Question, id=id_q)
        stage = Stage.objects.filter(question=question, stage_number=id_s).first()
        return render(request, 'question/question.html', {
            'question': question,
            'stage': stage,
        })

    def post(self, request, id_q, id_s):
        question = get_object_or_404(Question, id=id_q)
        stage = Stage.objects.filter(question=question, stage_number=id_s).first()

        selected_option = request.POST.get('option')
        correct_option = str(stage.correct_option)
        
        if selected_option == correct_option:
            
            message = "correct option"
            next_stage = Stage.objects.filter(question=question, stage_number=id_s + 1).first()
            
            if next_stage:
                return redirect('question:question_view', id_q=id_q, id_s=next_stage.stage_number)
            else:
                message = " finish the all stage og this question."
        
        else:
            message = "incorrect answer ridi dadash try again."
        
        return render(request, 'question/question.html', {
            'question': question,
            'stage': stage,
            'message': message
        })

