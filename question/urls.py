from django.urls import path
import question.views as views

app_name = 'question'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page_id>/', views.main, name='main_with_page'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:id>/', views.question, name='is'),
    path('tag/<str:tag>/', views.tag, name='tag'),
]
