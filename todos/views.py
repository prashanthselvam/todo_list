import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

logger = logging.getLogger("todos")

# Create your views here.

# List and add todos


def todo_list(request):
    logger.info("This is an info log")
    logger.error("This is an error log")
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Todo.objects.create(text=text)
        return redirect("todo_list")
    todos = Todo.objects.all().order_by("-id")
    return render(request, "todos/todo_list.html", {"todos": todos})


# Toggle completed


def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")


# Delete todo


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo_list")
