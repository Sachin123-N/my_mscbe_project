from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BillForm
from .models import Bill


@login_required(login_url="login_url")
def create_order(request):
    template_name = 'billapp/create.html'
    form = BillForm()
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = 'billapp/show.html'
    orders = Bill.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = Bill.objects.get(id=pk)
    form = BillForm(instance=obj)
    if request.method == "POST":
        form = BillForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, 'billapp/create.html', context)


def cancel_order(request, pk):
    obj = Bill.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'billapp/confirmation.html')
