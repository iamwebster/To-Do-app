from django.shortcuts import render, redirect
from .models import Task, Importance
from .forms import AddTaskForm, EditTaskForm
from django.core.paginator import Paginator
from django.db.models import Q


def notes_view(request):
    search = request.GET.get('search')
    tasks = Task.objects.filter(complete=False)
    if search:
        tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
    p = Paginator(tasks, 15)
    page = request.GET.get("page")
    tasks = p.get_page(page)
    context = {"tasks": tasks}
    return render(request, template_name="notes.html", context=context)


def category(request, imp):
    importance = Importance.objects.get(name=imp)
    tasks = Task.objects.filter(importance=importance)
    return render(
        request,
        "notes_importance.html",
        context={"tasks": tasks, "importance": importance},
    )


def add_task_view(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("notes")
        else:
            print("Error form validation")
    form = AddTaskForm()
    return render(request, "add_task.html", context={"form": form})


def detail_task_view(request, pk):
    form = AddTaskForm()
    if request.method == "POST":
        if len(request.POST) == 2:
            task = Task.objects.get(pk=pk)
            task.complete = True
            task.save()
            return redirect("notes")
    task = Task.objects.get(pk=pk)
    return render(request, "detail_page.html", context={"task": task, "form": form})


def delete_task_view(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("notes")


def completed_tasks_views(request):
    tasks = Task.objects.filter(complete=True)
    return render(request, "completed_tasks.html", context={"tasks": tasks})


def detail_complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "detail_completed_page.html", context={"task": task})


def edit_task_view(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == "POST":
        form = EditTaskForm(request.POST)
        if form.is_valid():
            task.description = request.POST["description"]
            task.save()
        else:
            print("Error form validation")

        return redirect("notes")
    form = EditTaskForm(instance=task)
    return render(request, "edit_task.html", context={"form": form, "task": task})
