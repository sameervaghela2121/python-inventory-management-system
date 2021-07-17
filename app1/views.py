from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Inventory,Register,Bill
# Create your views here.
def Index(request):
    if 'logged' in request.session.keys():
        usrnme = request.session['logged']
        nme = Register.objects.get(Username = usrnme)
    # data = Inventory.objects.all()
    # records = {'data':data}
        return render(request,'index.html',{'nme':nme})
    else:
        return redirect('login')

def Invoice(request):
    if 'logged' in request.session.keys():
        objinv = Inventory.objects.all()
        # objbill = Bill.objects.all()
        if request.POST:
            c_name = request.POST['C_Name']
            c_add = request.POST['C_Add']
            c_phone = request.POST['C_Phone']
            P_name = request.POST['C_Pro_Name']
            c_quant = request.POST['C_Quant']
            #P_quan = request.POST['quan']
            var = Inventory.objects.get(id = int(P_name))
            # var1 = Inventory.objects.get(id = int(P_quan))
            #print(var.Product_Name)

            objinvt = Inventory()
            objbill = Bill()
            objbill.C_Name = c_name
            objbill.C_Add = c_add
            objbill.C_Phone = c_phone
            objbill.C_Pro_Name = P_name
            objbill.C_Quant = c_quant
            objbill.save()
            var1 = Inventory.objects.get(id = int(P_name))
            i_quan = var.Product_Name - objbill.C_Quant
            print(i_quan)


        #print(c_name,c_add)
        return render(request,'invoicegenerator.html',{'objdict':objinv})
    else:
        return redirect('login')

def Invent(request):
    if 'logged' in request.session.keys():
        data = Inventory.objects.all()
        records = {'data':data}
        usrnme = request.session['logged']
        nme = Register.objects.get(Username = usrnme)
        return render(request,'inventory.html',{'Keys':data,'nme':nme})
    else:
        return redirect('login')

def Login(request):
    if request.POST:
        usrnme = request.POST['Username']
        pswd = request.POST['Password']
        print(usrnme,pswd)

        try:
            logged = Register.objects.get(Username = usrnme)
            if logged.Password == pswd:
                request.session['logged'] = usrnme
                return redirect('index')
            else:
                return HttpResponse('<h1>Password Wrong</h1>')
        except:
            return HttpResponse('<h1>Wrong Email </h1>')

    return render(request,'login.html')

def Logout(request):
    if 'logged' in request.session.keys():
        del request.session['logged']
        return redirect('login')
    else:
        return redirect('login')

