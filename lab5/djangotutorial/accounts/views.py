# Create your views here
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        # print(request)
        #
        # # --- The most useful attributes to print for debugging ---
        #
        # print(request.method)  # Outputs: 'GET' or 'POST'
        # print(request.user)  # Outputs: The logged-in user (or AnonymousUser)
        # print(request.POST)  # Outputs: A dictionary of submitted form data
        # print(request.GET)  # Outputs: A dictionary of URL parameters (?key=value)
        # print(request.headers)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/books/")
        else:
            return render(request, "authenticate/login.html", {})
    else:
        return render(request, "authenticate/login.html", {})


def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    else:
        form = UserCreationForm()
    return render(request, "authenticate/signup.html", {"form": form})
