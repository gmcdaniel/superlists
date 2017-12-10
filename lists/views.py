from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the_list/')

def view_list(request):
    items = Item.objects.all()
    todos = [ '{i}: {s}'.format(i=i, s=s.text)
        for i, s in enumerate(items, 1)]
    return render(request, 'list.html', {'items': todos})
