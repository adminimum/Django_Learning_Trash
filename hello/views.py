import re
from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect, \
    JsonResponse
from datetime import date
from django.shortcuts import render
import datetime
from .forms import UserForm
from .models import Person
from .models import Student, Course
from .models import Company, Product

def index_stud(request):
    # фильтрация
    students = Student.objects.all()
    return render(request, "index_stud.html", {"students":students})

def create_stud(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        course_ids = request.POST.getlist("courses")
        student.save()
        # получаем все выбранные курсы по их id
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses,  through_defaults={"date": date.today(), "mark":0})
        return HttpResponseRedirect("/index_stud")
    # передаем данные в шаблон
    courses = Course.objects.all()
    return render(request, "create_stud.html", {"courses": courses})

def initialize():
    # Student.objects.all().delete()
    # Course.objects.all().delete()
    if Course.objects.all().count() == 0:
        Course.objects.create(name = "Python")
        Course.objects.create(name = "Django")
        Course.objects.create(name = "FastAPI")
        Course.objects.create(name = "JAVA")
        Course.objects.create(name = "Flask")
        Course.objects.create(name = "Ruby")

def index_bd_multi(request):
    products = Product.objects.all()
    return render(request, "index_bd_multi.html", {"products": products})

def create_prod(request):
    create_companies()  # добавляем начальные данные для компаний
 
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/index_bd_multi")
    # передаем данные в шаблон
    companies = Company.objects.all()
    return render(request, "create_prod.html", {"companies": companies})

def edit_prod(request, id):
    try:
        product = Product.objects.get(id=id)
 
        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get("company")
            product.save()
            return HttpResponseRedirect("/index_bd_multi")
        else:
            companies = Company.objects.all()
            return render(request, "edit_prod.html", {"product": product, "companies": companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

def delete_prod(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/index_bd_multi")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
 
# добавление начальных данных в таблицу компаний
def create_companies():
      
     if Company.objects.all().count() == 0:
          Company.objects.create(name = "Apple")
          Company.objects.create(name = "Asus")
          Company.objects.create(name = "MSI")

def index_bd(request):
    people = Person.objects.all()
    return render(request, "index_bd.html", {"people": people})

def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/index_bd")

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/index_bd")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/index_bd")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def index_form(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = request.POST.get("age")
            comment = request.POST.get("comment")
            mina = request.POST.get("mina")
            pers = Person(name=name, age=age, comment=comment, mina=mina)
            print(pers)
            pers.save()
            return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}, mina: {mina}</h2>")
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "index_form.html", {"form": userform})

def index_post(request):
    return render(request, "index_post.html")

def postuser(request):
    # получаем из строки запроса имя пользователя
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])

    return HttpResponse(f"""
                <div>Name: {name}  Age: {age}<div>
                <div>Languages: {langs}</div>
            """)

def super_contacts(request):
    return render(request, "extend_contacts.html")

def index3(request):
    return render(request, "index2.html")

def index2(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
    body = "<h1>Hello World!</h1>"
    role = "Admin"
    date = datetime.datetime.now()

    data = {"header": header, "langs": langs, "user": user, "address": address, "body": body, "role":role,"date":date}
    return render(request, "index_site.html", context=data)

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>User-agent: {user_agent}</p>
    """,headers = {"SecretCode": "ILoveDasha"})

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("Контакты")

def error400(request):
    return HttpResponse("Some error happened",status = 400, reason="Incorrect request")

def access(request, age):
    if age in range(1, 111) and age > 17:
        return HttpResponse("Access given")
    else:
        return  HttpResponseBadRequest("Incorrect data")

def user(request,name=None,age=None):
    people = ["bob","max","dash"]
    if name in people:
        return HttpResponse(f"""<h2>Name: {name}</h2>
            <h2>Age {age}</h2>""")
    else:
        return HttpResponseNotFound("User not found")

def products(request,id):
    return HttpResponse(f"Product {id}")
 
def comments(request,id):
    return HttpResponse(f"Comment about product {id}")
 
def questions(request,id):
    return HttpResponse(f"Question about product {id}")

def user_params(request):
    name = request.GET.get("name")
    id   = request.GET.get("id")
    return HttpResponse(f"""
    <p>Name: {name}</p>
    <p>ID: {id}</p>
    """)

def redirect(request):
    return HttpResponseRedirect("/user_with_params?name=max&id=11")

def per_redirect(request):
    return HttpResponsePermanentRedirect("/user")
