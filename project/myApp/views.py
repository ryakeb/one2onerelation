from django.shortcuts import render, redirect
from myApp.forms import (
    PresidentForm,
    CountryForm,
    UserForm,
    ProjectForm,
    TaskForm,
    QuestionForm,
    AnswerForm,
)
from myApp.models import President, Country, User, Project, Task, Question, Answer


# Create your views here.
def home(request):
    president = President.objects.all()
    country = Country.objects.all()
    context = locals()
    return render(request, "myApp/home.html", context)


def create_president(request):
    if request.method == "POST":
        form = PresidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PresidentForm()
    return render(
        request, "myApp/backoffice/forms/create_president.html", {"form": form}
    )


def create_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CountryForm()
    return render(request, "myApp/backoffice/forms/create_country.html", {"form": form})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = UserForm()
    return render(request, "myApp/backoffice/forms/create_user.html", {"form": form})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = ProjectForm()
    return render(request, "myApp/backoffice/forms/create_project.html", {"form": form})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = TaskForm()
    return render(request, "myApp/backoffice/forms/create_task.html", {"form": form})


def users(request):
    users = User.objects.all()
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {"users": users, "projects": projects, "tasks": tasks}
    return render(request, "myApp/users.html", context)




# QUIZZ-------------------------------------

def quizz(request):
    question = Question.objects.all().order_by('id')
    quizz_data = [(question, Answer.objects.filter(question=question)) for question in question]
    context = {"quizz_data": quizz_data}
    return render(request, "myApp/quizz.html", context)


def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question")
    else:
        form = QuestionForm()
    return render(
        request, "myApp/backoffice/forms/create_question.html", {"form": form}
    )


def create_answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("answer")
    else:
        form = AnswerForm()
    return render(request, "myApp/backoffice/forms/create_answer.html", {"form": form})





