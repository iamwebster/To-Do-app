from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTaskForm


def notes_view(request):
    tasks = Task.objects.filter(complete=False)
    context = {"tasks": tasks}
    return render(request, template_name="notes.html", context=context)


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
    return redirect('notes')


def completed_tasks_views(request):
    tasks = Task.objects.filter(complete=True)
    return render(request, 'completed_tasks.html', context={'tasks': tasks})


def detail_complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'detail_completed_page.html', context={'task': task})