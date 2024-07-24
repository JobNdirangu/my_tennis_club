from django.shortcuts import render, redirect
from .forms import * 
from .models import Employee
from members.models import *
from django.contrib import messages
from django.db.models import Count, Sum
# Create your views here.
def saveemployee(request):
    if request.method== "POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("employees")
            except:
                pass
    else:
        form=EmployeeForm()
        return render(request,'saveemp.html',{'form':form})

def employees(request):
        employees = Employee.objects.all()
        return render(request, "employees.html", {'employees': employees})

def delete_emp(request,employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        employee.delete()
        messages.success(request, 'Employee has been deleted successfully.')
        return redirect('employees')
    except Employee.DoesNotExist:
        messages.error(request, 'Employee does not exist.')
        return redirect('employees')

def update_emp(request,employee_id):
    if request.method=='POST':
        print('the id is:', employee_id)
        employee= Employee.objects.get(employee_id=employee_id)
        print(employee)
        
        form= EmployeeForm(request.POST,instance=employee)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful.')
            return redirect('employees')
        else:
            messages.error(request, 'Update failed.')
            return redirect('employees')
    else:
        employee = Employee.objects.get(employee_id=employee_id)
        return render(request,"updateemp.html",{'employee':employee})


#kit 
def kitview(request):
        kit = TrainingKitCollection.objects.all()
        return render(request, "kitview.html", {'kits': kit})
    
def addkit(request):
    if request.method == "POST":
        form = TrainingKitCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kitview") 
        else:
            pass # Redirect to a view named 'kitview' upon successful form submission
    else:
        form = TrainingKitCollectionForm()
    return render(request, 'kitadd.html', {'form': form})

def update_kit(request,kit_id):
    kit= TrainingKitCollection.objects.get(kit_id=kit_id)  
    if request.method=='POST':      
        form= TrainingKitCollectionForm(request.POST,instance=kit)
        print('first test')
        
        if form.is_valid():
            print('form test')
            form.save()
            messages.success(request, 'Update Successful.')
            return redirect('kitview')
        else:
            print(form.errors)
            messages.error(request, 'Update failed.')
            return redirect('kitview')
    else:
        player=Player.objects.all()
        return render(request,"kitupdate.html",{'kit':kit,'players':player})


def delete_kit(request,kit_id):
    try:
        kit = TrainingKitCollection.objects.get(kit_id=kit_id)
        kit.delete()
        messages.success(request, 'Kit has been deleted successfully.')
        return redirect('kitview')
    except kit.DoesNotExist:
        messages.error(request, 'kit does not exist.')
        return redirect('kitview')


# Player
def playerview(request):
        player = Player.objects.all()
        return render(request, "playerview.html", {'players': player})

def addplayer(request):
    if request.method== "POST":
        form=PlayerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("playerview")
            except:
                pass
    else:
        form=PlayerForm()
        return render(request,'playeradd.html',{'form':form})

def update_player(request,player_id):
    if request.method=='POST':
        player= Player.objects.get(player_id=player_id)
        
        form= PlayerForm(request.POST,instance=player)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful.')
            return redirect('playerview')
        else:
            messages.error(request, 'Update failed.')
            return redirect('playerview')
    else:
        player = Player.objects.get(player_id=player_id)
        club=Club.objects.all()
        trainer=Trainer.objects.all()
        return render(request,"playerupdate.html",{'player':player,'clubs':club,'trainers':trainer})


def delete_player(request,player_id):
    try:
        employee = Player.objects.get(player_id=player_id)
        employee.delete()
        messages.success(request, 'Player has been deleted successfully.')
        return redirect('playerview')
    except Player.DoesNotExist:
        messages.error(request, 'Player does not exist.')
        return redirect('playerview')


def dashboard(request):
    players= Player.objects.aggregate(player_count=Count('player_id'))
    player_count=players['player_count']

    employees= Employee.objects.aggregate(employees_count=Count('employee_id'))
    employees_count=employees['employees_count']

    payments= Payment.objects.aggregate(payment_sum=Sum('amount'))
    payment_sum=payments['payment_sum']

    return render(request, "dashboard.html",{'player_count':player_count,"employees_count":employees_count,"payment_sum":payment_sum})