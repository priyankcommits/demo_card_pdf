from django.shortcuts import render
from django.http import HttpResponse
from .forms import IDForm
from .utils import Generate_PDF

import os

def card_pdf(request):
    if request.method == 'GET':
        form = IDForm()
    else:
        first_name = request.POST.get("first_name", "example")
        last_name = request.POST.get("last_name", "example")
        id_emp = request.POST.get("id", "000")
        age = request.POST.get("age", "0")
        sex = request.POST.get("sex","M")
        try:
            file_name = Generate_PDF(first_name, last_name, id_emp, age, sex,)
            data = open(file_name,"rb").read()
            return HttpResponse(data, content_type="application/pdf")
        except:
            return HttpResponse("Something went wrong,contact admin")
        finally:
            os.remove(file_name)

    return render(request, "democard/form.html", { "form": form })

