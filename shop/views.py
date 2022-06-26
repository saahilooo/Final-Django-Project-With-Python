from django.shortcuts import render, redirect
from shop.forms import ShopForm
from shop.models import Shop


# Create Shop:

def createShop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
            pass
    else:
        form = ShopForm()
    return render(request, "index.html", {'form': form})


def show(request):
    shops = Shop.objects.all()
    return render(request, "show.html", {"shops": shops})


def edit(request, id):
    shop = Shop.objects.get(id=id)

    return render(request, "edit.html", {"shop": shop})


def update(request, id):
    shop = Shop.objects.get(id=id)
    form = ShopForm(request.POST, instance=shop)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {"shop": shop})

def delete(request, id):
    shop = Shop.objects.get(id=id)
    shop.delete()
    return redirect('/show')