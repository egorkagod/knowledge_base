from django.shortcuts import render
from django.core.paginator import Paginator

questions = {
        1: {
            'id': 1,
            'title': 'How to create your own proxy server',
            'content': "The Iron Curtain is not on fire...",
            'tags': ['server', 'proxy'],
        },
        2: {
            'id': 2,
            'title': "Mom took the lan cable, what should I do",
            'content': "Guys, I recently wrote a post about database caricature, but I couldn't post it because...",
            'tags': ['server'],
        }
}
for i in range(20):
    questions[3+i] = {
        'id': 3 + i,
        'title': 'A simple title',
        'content': "A simple description",
        'tags': [],
    }

def main(request, page_id=1):
    paginator = Paginator(list(questions.values()), 5)
    if page_id > paginator.num_pages: page_id = 1
    page = paginator.get_page(page_id)
    return render(request, 'question/main.html', context={'questions': page.object_list, 'pages': range(1, paginator.num_pages+1)})

def ask(request):
    return render(request, 'question/new-question.html')

def question(request, id):
    return render(request, 'question/question.html', context={'question': questions[id]})

def tag(request, tag):
    data = [question for question in questions.values() if tag in question['tags']]
    return render(request, 'question/tag.html', context={'questions': data, 'tag': tag})