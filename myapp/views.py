from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Position,Employee
from myapp.forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def Employee_list(request):
    employee=Employee.objects.all()
    context={
    'employee':employee
    }
    return render(request,'myapp/Employee_list.html',context)
@login_required
def Employee_details(request,id):
    employee_obj=Employee.objects.get(id=id)
    context={
    'employee':employee_obj
    }
    return render(request,'myapp/Employee_details.html',context)

@login_required
def Employee_form(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form=EmployeeForm()
    context={
    'form':form
    }
    return render(request,'myapp/Employee_form.html',context)
@login_required
def Employee_update(request,id):
    instance=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance.save()
        return HttpResponseRedirect('/')
    context={
    'form':form
    }
    return render(request,'myapp/Employee_update.html',context)
@login_required
def Employee_delete(request,id):
    instance=Employee.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/')
    context={
    'instance':instance
    }
    return render(request,'myapp/Employee_delete.html',context)
