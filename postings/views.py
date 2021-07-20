from django.shortcuts import render
from .forms import MessageForm
from .models import Messages


def allmessages(request):
    messages = Messages.objects.all().order_by("-id")
    return render(request, "allmessages.html", {"messages": messages})


def index(request):
    is_posted = False
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            messages = Messages()
            if form.data["username"] != "":
                messages.username = form.cleaned_data["username"]
            messages.message = form.cleaned_data["message"]
            messages.save()
            form = MessageForm()
            is_posted = True
            return render(request, "index.html", {"form": form, "is_posted": is_posted})

    form = MessageForm()
    return render(request, "index.html", {"form": form, "is_posted": is_posted})
