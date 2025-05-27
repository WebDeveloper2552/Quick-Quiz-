from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import TeacherSignUpForm, StudentSignUpForm
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'teacher'):
                    return redirect('teacher_dashboard')
                else:
                    return redirect('student_dashboard')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        if 'teacher_signup' in request.POST:
            teacher_form = TeacherSignUpForm(request.POST)
            if teacher_form.is_valid():
                teacher_form.save()
                messages.success(request, 'Teacher account created successfully!')
                return redirect('login')
        else:
            student_form = StudentSignUpForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                messages.success(request, 'Student account created successfully!')
                return redirect('login')
    else:
        teacher_form = TeacherSignUpForm()
        student_form = StudentSignUpForm()
    return render(request, 'signup.html', {
        'teacher_form': teacher_form,
        'student_form': student_form
    })

# Teacher Views
@login_required
def teacher_dashboard(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('student_dashboard')
    return render(request, 'teacher_dashboard.html')

@login_required
def manage_quizzes(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('student_dashboard')
    return render(request, 'manage_quizzes.html')

@login_required
def create_quiz(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('student_dashboard')
    return render(request, 'create_quiz.html')

@login_required
def class_tracker(request):
    if not hasattr(request.user, 'teacher'):
        return redirect('student_dashboard')
    return render(request, 'class_tracker.html')

# Student Views
@login_required
def student_dashboard(request):
    if hasattr(request.user, 'teacher'):
        return redirect('teacher_dashboard')
    return render(request, 'student_dashboard.html')

@login_required
def join_quiz(request):
    if hasattr(request.user, 'teacher'):
        return redirect('teacher_dashboard')
    return render(request, 'join_quiz.html')

@login_required
def student_results_view(request):
    if hasattr(request.user, 'teacher'):
        return redirect('teacher_dashboard')
    return render(request, 'student_results.html')

# Shared Views
@login_required
def ai_chatbot(request):
    return render(request, 'ai_chatbot.html')

@login_required
def student_results(request, student_id):
    if not hasattr(request.user, 'teacher'):
        return redirect('student_dashboard')
    # Add logic to fetch specific student results
    return render(request, 'student_results_detail.html', {'student_id': student_id})
