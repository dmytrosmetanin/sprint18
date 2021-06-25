from django.shortcuts import render, redirect

from .models import CustomUser
from .user_form import UserForm


def user_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = CustomUser.get_by_id(id)
            form = UserForm(instance=user)
        return render(request, 'authentication/user_form.html', {'form': form})
    if request.method == "POST":
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.get_by_id(id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('authentication:user_list')


def user_delete(request, id):
    CustomUser.delete_by_id(id)
    return redirect('authentication:user_list')


def user_list(request):
    all_users = CustomUser.get_all()
    return render(request, 'authentication/all_users.html', {'all_users': all_users})
