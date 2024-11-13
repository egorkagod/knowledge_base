from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question


def paginate(objects_list, page_id=1, per_page=10):
    paginator = Paginator(objects_list, per_page, allow_empty_first_page=True)
    page = paginator.get_page(page_id)
    return page

def main(request, page_id=1):
    new_questions = Question.objects.new()
    page = paginate(new_questions, page_id, per_page=5)
    return render(request, 'question/main.html', context={'questions': page.object_list})

def hot(request, page_id=1):
    hot_questions = Question.objects.hot()
    page = paginate(hot_questions, page_id, per_page=5)
    return render(request, 'question/main.html', context={'questions': page.object_list})

def ask(request):
    return render(request, 'question/new-question.html')

def question(request, id):
    q = Question.objects.get(pk=id)
    return render(request, 'question/question.html', context={'question': q})

def tag(request, tag):
    questions = Question.objects.tag(tag)
    return render(request, 'question/tag.html', context={'questions': questions, 'tag': tag})

