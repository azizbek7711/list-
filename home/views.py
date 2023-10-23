from django.shortcuts import render, redirect
from  .models import *

# Create your views here.
def student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get("photo")
        Category.objects.create(
            name = name,
            photo = photo,
        )
        return redirect("student")
    context = {
        "category":Category.objects.all()
    }
    return render(request, 'student.html',context)

def talaba(request):

    if request.method == "POST":
        name = request.POST.get("name")
        title = request.POST.get("title")
        date = request.POST.get("date")
        category = request.POST.get("category")
        Student.objects.create(
            name=name,
            title = title,
            date = date,
            category_id = category
        )
        return redirect('talaba')
    context = {
        "category":Category.objects.all(),
        "student":Student.objects.all()
    }
    return render(request, 'talaba.html',context)

def talaba_delete(request, pk):
    Student.objects.get(id=pk).delete()
    return redirect('talaba')

def talaba_update(request, pk):
    if request.method == 'POST':
        name = request.POST.get("name")
        title = request.POST.get("title")
        date = request.POST.get("date")
        category = request.POST.get("category")
        student = Student.objects.get(id=pk)
        student.name = name
        student.title = title
        student.date = date
        student.category = Category.objects.get(id=category)
        student.save()
        return redirect("talaba-update", pk)
    context ={
        "student":Student.objects.get(id=pk),
        "category": Category.objects.all(),
    }
    return render(request, 'talaba-update.html', context)

def order(request):
    order = Order.objects.all()
    context={
        "order":order
    }
    return render(request, 'order.html',context)

def order_delete(request,pk):
    Order.objects.get(id=pk).delete()
    return redirect('order')


def order_update(request, pk):
    return render(request, 'order_update.html')