from django.shortcuts import redirect, render
import user
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/course')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form}) 
    