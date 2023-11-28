from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTaskForm


def notes_view(request):
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request, template_name='notes.html', context=context)


def add_task_view(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('notes')
        else:
            print('Error form validation')
    form = AddTaskForm()
    return render(request, 'add_task.html', context={'form': form})