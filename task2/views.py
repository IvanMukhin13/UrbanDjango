from django.shortcuts import render


# Create your views here.


def index_class(request):
    return render(request, 'second_task/class_templates.html')


def index_func(request):
    return render(request, 'second_task/func_templates.html')
