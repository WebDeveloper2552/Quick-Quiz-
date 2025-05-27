from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    
    # Teacher URLs
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/quizzes/', views.manage_quizzes, name='manage_quizzes'),
    path('teacher/quizzes/create/', views.create_quiz, name='create_quiz'),
    path('teacher/class-tracker/', views.class_tracker, name='class_tracker'),
    path('teacher/student/<int:student_id>/', views.student_results, name='student_results'),
    
    # Student URLs
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/join-quiz/', views.join_quiz, name='join_quiz'),
    path('student/results/', views.student_results_view, name='student_results'),
    
    # Shared URLs
    path('ai-chatbot/', views.ai_chatbot, name='ai_chatbot'),
]
