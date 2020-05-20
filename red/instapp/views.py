from django.shortcuts import render
from .froms import User_form
# Create your views here.
def index(request):
    form = User_form()
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request,'index.html',{'form':form})
