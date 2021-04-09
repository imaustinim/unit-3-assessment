from django.shortcuts import render, redirect
from .models import Widget, WidgetForm
from django.db.models import Sum
# Create your views here.

def index(request):
    if request.method == "GET":
        widgets = Widget.objects.all()
        quantity_total = Widget.objects.all().aggregate(Sum("quantity"))["quantity__sum"]
        return render(request, 'home.html', {
            "widgets" : widgets,
            "form" : WidgetForm(),
            "quantity_total" : quantity_total
        })
    elif request.method== "POST":
        print(request.POST)
        widget = Widget.objects.create(
            description = request.POST["description"],
            quantity = int(request.POST["quantity"])
        )
        return redirect("/")

def delete_widget(request, id):
    widget = Widget.objects.get(id=id)
    widget.delete()
    return redirect("/")
