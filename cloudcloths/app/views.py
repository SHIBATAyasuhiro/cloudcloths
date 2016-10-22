from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class AccountCreateView(CreateView):
    model = User

    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('app:user_creation')


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm

    def get_success_url(self):
        return reverse('my:user_change', args=(self.object.id, ))


def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:8]
    context = {
        'latest_product_list': latest_product_list,
        'user': request.user
    }
    return render(request, 'app/index.html', context)


def list(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:8]
    context = {
        'latest_product_list': latest_product_list
    }
    return render(request, 'app/list.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'app/detail.html', {'product':product})




