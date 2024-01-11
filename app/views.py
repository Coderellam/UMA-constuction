from django.shortcuts import render, redirect
from .models import AboutCompany, Contact, Project, MainPage
import requests
from django.http import HttpResponse


def home_view(request):
    data = request.GET

    main = AboutCompany.objects.all()
    p = {
        'main': main
    }
    return render(request, 'home.html', p)


def service_view(request):
    return render(request, 'services.html')


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    if request.method == "POST":
        data = request.POST
        obj = Contact.objects.create(name=data['name'], phone_number=data['number'], message=data['message'])

        obj.save()
        url = f"https://api.telegram.org/bot6298724589:AAHQn4M1fxewf_9bSlDQAkPi5jvS2GzPGnk/sendMessage?chat_id=748076346&text=you have a notification from UMA construction: {data['message']} ." \
              f" Phone number of a sender is {data['number']}"
        requests.get(url)
        return redirect('/')

    return render(request, "contact.html")


def project_view(request):
    data = request.GET

    main = AboutCompany.objects.all()
    p = {
        'main': main
    }
    return render(request, 'projects.html', p)


def projects_single_view(request, pk):
    project = Project.objects.get(id=pk)
    d = {
        'project': project

    }

    if request.method == "POST":
        data = request.POST
        obj = Project.objects.create(project_name=data['name'], description=data['description'])

        obj.save()

        return redirect(f'/projects/{pk}')

    return render(request=request, template_name="projects-single.html", context=d)
