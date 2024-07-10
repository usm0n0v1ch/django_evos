from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from evos_app.models import Category, Food, Basket


def control_panel(request):
    return render(request, 'evos_app/control_panel.html')


def control_panel_categories(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories,
    }
    return render(request, 'evos_app/control_panel_categories.html',context=ctx)
def control_panel_foods(request):
    foods = Food.objects.all()
    ctx = {
        'foods': foods,
    }
    return render(request, 'evos_app/control_panel_foods.html',context=ctx)
def control_panel_users(request):
    users = User.objects.all()
    ctx = {
        'users': users,
    }
    return render(request, 'evos_app/control_panel_users.html',context=ctx)

def menu(request):
    categories = Category.objects.all()
    foods = Food.objects.all()
    ctx = {
        'categories': categories,
        'foods': foods,
    }
    return render(request, 'evos_app/menu.html', context=ctx)


def menu_by_category(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    foods = Food.objects.filter(category=category)
    ctx = {
        'categories': categories,
        'foods': foods,
    }
    return render(request, 'evos_app/menu.html', context=ctx)

def basket(request):
    return render(request, 'evos_app/basket.html')


def profile(request):
    return render(request, 'evos_app/profile.html')

def add_to_basket(request,pk):
    food = Food.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    basket = get_object_or_404(Basket, user=request.user, food=food)
    if basket:
        basket.food_quantity+=1
        basket.save()
    else:
        basket = Basket(user=request.user, food=food, food_quantity=1)
        basket.save()
