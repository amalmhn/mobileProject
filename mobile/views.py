from django.shortcuts import render, redirect
from .forms import MobileCreateForm
from .models import MobileModel
# Create your views here.

def mobile_create(request):
    form = MobileCreateForm()
    context = {}
    context['form'] = form
    mobile = MobileModel.objects.all()
    context['mobile'] = mobile
    if request.method == 'POST':
        form = MobileCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            context['form'] = form
            return render(request, 'mobile/index.html', context)
    return render(request,'mobile/index.html',context)

def demo(request):
    return render(request,'mobile/createPhone.html')
