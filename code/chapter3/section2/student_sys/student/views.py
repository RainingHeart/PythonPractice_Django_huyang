from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student.forms import StudentForm
from .models import Student


# Create your views here.
# def index(request):
#     students = Student.objects.all()
#     return render(request, 'index.html', context={'students': students})

# def index(request):
#     students = Student.objects.all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         print('*****************', request.POST, '********************')
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             student = Student()
#             student.name = cleaned_data['name']
#             student.sex = cleaned_data['sex']
#             student.email = cleaned_data['email']
#             student.profession = cleaned_data['profession']
#             student.qq = cleaned_data['qq']
#             student.phone = cleaned_data['phone']
#             student.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentForm()
#
#     context = {
#         'students': students,
#         'form': form,
#     }
#     return render(request, 'index.html', context=context)

def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)
