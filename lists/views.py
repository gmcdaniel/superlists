from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the_list/')

    items = Item.objects.all()
    #return render(request, 'home.html', {'items': items})
    todos = [ '{i}: {s}'.format(i=i, s=s.text)
        for i, s in enumerate(items, 1)]
    return render(request, 'home.html', {'items': todos})

def view_list(request):
    items = Item.objects.all()
    todos = [ '{i}: {s}'.format(i=i, s=s.text)
        for i, s in enumerate(items, 1)]
    return render(request, 'list.html', {'items': todos})
