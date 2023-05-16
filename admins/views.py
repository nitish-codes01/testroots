from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from admins.models import Users,Roles,Product,Admin,Crops,privacypolicy,Termcondition,AboutUs,Settings,buyeroffers,farmeroffers,Transactions,Logisticsoffers,FieldIssue
from django.db import connection
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import datetime
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import html,cgi
from geopy.geocoders import Nominatim



# Create your views here.
em=''
pwd=''
name=''
fname=''
mob=''
ids=''
aadhar=''
image=''

def send_json(request):

    pas = base64.urlsafe_b64decode('Z0FBQUFBQmtLb2tIYkhXcnBxbnZEMTdqN0hyeWN6N1dJQVNFTVcwS2VTS3hDT3ctS01RRktsa2pSMnZGVXZyb0paUVBrNzhWdzRfdlk0VEY0dERNdlo4b2pjSWFITEsxa0E9PQ==')
    cipher_pass = Fernet(settings.ENCRYPT_KEY)
    decod_pass = cipher_pass.decrypt(pas).decode("ascii")  
    print(decod_pass)

def login(request):
    settings=Settings.objects.filter(id='1')
    data={
        'adminsettings':settings
    }
    return render(request,'enroll/admin/login.html',data)

def adminlogin(request):
        settingss=Settings.objects.filter(id='1')
        data={
            'error':''
        }
        if request.method=="POST":
            email=request.POST.get('email')
            if email:
                password=request.POST.get('password')
                if password:
                    print(email, password)
                    user=Admin.objects.filter(email=email)
                    
                    if user:
                        print('hi')
                        user=Admin.objects.get(email=email)
                        print(user.password)
                        pas = base64.urlsafe_b64decode(user.password)
                        cipher_pass = Fernet(settings.ENCRYPT_KEY)
                        decod_pass = cipher_pass.decrypt(pas).decode("ascii")     
                        
                        # print(flag.password)
                        if password==decod_pass:
                            request.session['admin_id']=user.id
                            request.session['admin_email']=user.email
                            request.session['admin_username']=user.username
                            request.session.set_expiry(7200)
                            data={
                                'adminsettings':settingss,
                                'msgflash':'successfully Login '+user.username
                            }
                            print(data)
                            return render(request,'enroll/admin/login.html',data)
                            # return HttpResponseRedirect('/dash')
                        else:
                            data={
                            'adminsettings':settingss,
                            'error':"Password is Incorrect",
                            'email':email
                        }
                        return render(request,'enroll/admin/login.html',data)
                    else:
                        data={
                            'adminsettings':settingss,
                            'error':"Email is Incorrect",
                            'email':email
                        }
                        return render(request,'enroll/admin/login.html',data)
                else:
                    data={
                            'adminsettings':settingss,
                            'error':"Password is Incorrect",
                            'email':email
                    }
                    return render(request,'enroll/admin/login.html',data)
            else:
                data={
                        'adminsettings':settingss,
                        'error':"Email is Required",
                        'email':email
                }
                return render(request,'enroll/admin/login.html',data)
        return render(request,'enroll/admin/login.html',data)
    
def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return HttpResponseRedirect('/')

def dashboard(request):
    id=request.session.get('admin_id')
    username=request.session.get('admin_username')
    if id is not None:
        buyers=Users.objects.filter(roll_id='2').count
        farmers=Users.objects.filter(roll_id='1').count
        logistics=Users.objects.filter(roll_id='3').count
        admin=Admin.objects.filter(id=id)
        setting=Settings.objects.filter(id='1')
        data={
            'loginuser':username,
            'farmercount':farmers,
            'buyercount':buyers,
            'logisticscount':logistics,
            'admindata':admin,
            'adminsettings':setting
        }
        return render(request,'enroll/index.html',data)
    else:
        return HttpResponseRedirect('/')

def profileview(request):
    
    id=request.session.get('admin_id')
    result=Admin.objects.get(id=id)
    settingss=Settings.objects.filter(id='1')
    # flag=check_password(result.password)
    print('===================================')
    print(result.password)
    pas = base64.urlsafe_b64decode(result.password)
    cipher_pass = Fernet(settings.ENCRYPT_KEY)
    decod_pass = cipher_pass.decrypt(pas).decode("ascii")
    print('===================================')
    print(decod_pass)
    cars = [result.username,result.email]
    results=Admin.objects.filter(id=id)
    data={
        'password':cars,
        'admindata':results,
        'pass':decod_pass,
        'image':result.image,
        'adminsettings':settingss
    }
    print(data)
    return render(request,'enroll/admin/editprofile.html',data)

def profileupdate(request):
    global em,pwd,name,mob
    if request.method=="POST":
        cursor = connection.cursor()
        name=request.POST.get('name')
        email=request.POST.get('email')
        # password='12345678'
        # hashpassword=make_password(password)
        if 'image' in request.FILES:
            image=request.FILES['image']
            mobile=request.POST.get('mobile')
            # pas = str(password)
            # cipher_pass = Fernet(settings.ENCRYPT_KEY)
            # encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
            # encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
            d=request.POST
            cursor = connection.cursor()
            member = Admin.objects.get(id=1)
            member.username = name
            # member.password = encrypt_pass
            member.email = email
            member.image = image
            member.phone = mobile
            member.save()
            return HttpResponseRedirect('/profile/view/')
        else:
            # image=request.FILES['image']
            mobile=request.POST.get('mobile')
            # pas = str(password)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
            encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
            d=request.POST
            cursor = connection.cursor()
            member = Admin.objects.get(id=1)
            member.username = name
            member.password = encrypt_pass
            member.email = email
            # member.image = image
            member.phone = mobile
            member.save()
            return HttpResponseRedirect('/profile/view/')
    else:
            return HttpResponse('You have in get method')
    
def adminuser(request):
    id=request.session.get('admin_id')
    print(id)
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id=1)
    data={
        'adminsettings':settings,
        'admindata':admin
    }
    print(data)
    return render(request,'enroll/admin/adduser.html',data)

def adminuserlist(request):
    id=request.session.get('admin_id')
    print(id)
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id=1)
    alladmin=Admin.objects.all()
    data={
        'adminsettings':settings,
        'admindata':admin,
        'adminalldata':alladmin
    }
    print(data)
    return render(request,'enroll/admin/adminlist.html',data)

def adminsaveuser(request):
    if request.method=="POST":
        cursor = connection.cursor()
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('phone')
        if 'image' in request.FILES:
            image=request.FILES['image']
            pas = str(password)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
            encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
            # sql = """INSERT INTO user(name, email, mobile, password, aadharno,fathername,status)VALUES ('name', 'email', 'password', 'mobile', 'aadharno','fathername','1')"""
            admin=Admin(username=name,email=email,status=1,password=encrypt_pass,phone=mobile,image=image)
            admin.save()
        else:
            pas = str(password)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
            encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
            # sql = """INSERT INTO user(name, email, mobile, password, aadharno,fathername,status)VALUES ('name', 'email', 'password', 'mobile', 'aadharno','fathername','1')"""
            admin=Admin(username=name,email=email,status=1,password=encrypt_pass,phone=mobile)
            admin.save()
        return HttpResponseRedirect('/admins/list/user/')
    else:
        return HttpResponse('You have in get method')


# =============user section start==========================

def useradd(request):
    result=Roles.objects.all()
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        'abc':result,
        'admindata':admin,
        'adminsettings':settings
    }
    return render(request,'enroll/user/adduser.html',data)

def savedemouser(request):
    if request.method=="POST":
        cursor = connection.cursor()
        name=request.POST.get('name')
        fathername=request.POST.get('fathername')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('phone')
        aadharno=request.POST.get('aadhar')
        role=request.POST.get('role')
        pas = str(password)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
        # sql = """INSERT INTO user(name, email, mobile, password, aadharno,fathername,status)VALUES ('name', 'email', 'password', 'mobile', 'aadharno','fathername','1')"""
        add_user = ("INSERT INTO users "
                "(name, email, mobile, password, aadharno,fathername,status,roll_id) "
                "VALUES (%s, %s, %s, %s, %s, %s,%s,%s)")

        data_user = (name, email, mobile, encrypt_pass, aadharno,fathername,1,role)
        
        try:
            # Executing the SQL command
            cursor.execute(add_user,data_user)
            print('aaaaaaaaaaaaaaaaaaa')
            # strs = cursor.query
            # ptint(strs)
            print(data_user)
            print('aaaaaaaaaaaaaaaaaaa')
            # Commit your changes in the database
            connection.commit()
            return HttpResponseRedirect('/user/list/')

        except:
            # Rolling back in case of error
            connection.rollback()
    else:
        return HttpResponse('You have in get method')

def userlist(request , id):
    cursor = connection.cursor()
    cursor.execute("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.roll_id!=2")
    
    myresult = cursor.fetchall()
    id=request.session.get('admin_id')
    settings=Settings.objects.filter(id='1')
    admin=Admin.objects.filter(id=id)
    data={
        'abc':myresult,
        'admindata':admin,
        'adminsettings':settings
    }
    print(data)
    return render(request,'enroll/user/userlist.html',data)

# def userdelete(request):
#     id=request.GET.get('id')
#     cursor = connection.cursor()
#     cursor.execute("DELETE FROM users WHERE id="+id)
    
#     myresult = cursor.fetchall()
#     return HttpResponseRedirect('/user/list')

def userdelete(request):
    id=request.GET.get('id')
    member = Users.objects.get(id=id)
    role=member.roll_id
    member.status = '2'
    member.save()
    return HttpResponseRedirect('/user/byrole/'+role)

def edituser(request):
    id=request.GET.get('id')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id="+id)
    result=Users.objects.get(id=id)
    print(result)
    pas = base64.urlsafe_b64decode(result.password)
    cipher_pass = Fernet(settings.ENCRYPT_KEY)
    decod_pass = cipher_pass.decrypt(pas).decode("ascii")
    print(decod_pass)
    
    ids=request.session.get('admin_id')
    settingss=Settings.objects.filter(id='1')
    myresult = cursor.fetchall()
    admin=Admin.objects.filter(id=ids)
    data={
        'abc':myresult,
        'password':decod_pass,
        'admindata':admin,
        'adminsettings':settingss
    }
    return render(request,'enroll/user/updateuser.html',data)

def updateuser(request):
    global em,pwd,name,fname,mob,ids,aadhar
    if request.method=="POST":
        cursor = connection.cursor()
        id=request.POST.get('id')
        name=request.POST.get('name')
        fathername=request.POST.get('fathername')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('phone')
        aadharno=request.POST.get('aadhar')
        hashpassword=make_password(password)
        d=request.POST
        cursor = connection.cursor()
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="name":
                name=value
            if key=="fathername":
                fname=value
            if key=="phone":
                mob=value
            if key=="id":
                ids=value
            if key=="aadhar":
                aadhar=value
            print('====================================')
            print(ids)
            print('====================================')
        c="UPDATE `users` SET `name`='{}',`email`='{}',`password`='{}',`mobile`='{}',`fathername`='{}',`aadharno`='{}' WHERE `id`= '{}'".format(name,em,pwd,mob,fname,aadhar,ids)
        ac=cursor.execute(c)
        print(c)
        if ac==():
            return HttpResponse('Email Or Password is Incorrect')
        else:
            return HttpResponseRedirect('/user/list/')
        connection.commit()
    else:
            return HttpResponse('You have in get method')

def userbyrole(request ,role):
    cursor = connection.cursor()
    roleid=str(role)
    # print(role)
    cursor = connection.cursor()
    cursor.execute("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.status!=2 &&  users.roll_id="+roleid)
    # print("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.roll_id!=2 &&  users.roll_id="+roleid)
    myresult = cursor.fetchall()
    id=request.session.get('admin_id')
    settings=Settings.objects.filter(id='1')
    getrole=Roles.objects.get(id=roleid)
    admin=Admin.objects.filter(id=id)
    data={
        'abc':myresult,
        'adminsettings':settings,
        'admindata':admin,
        'rolename':getrole.name
    }
    return render(request,'enroll/user/usertypelist.html',data)

# =================user section end================================

# ===================crop section start============================

def addcrop(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    
    settings=Settings.objects.filter(id='1')
    data={
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/crop/addcrop.html',data)

def savecrop(request):
    global name,image
    if request.method=="POST":
        cursor = connection.cursor()
        name=request.POST.get('name')
        image=request.FILES['image']
        d=request.POST
        crop=Crops(name=name,image=image,status=1)
        crop.save()
        return HttpResponseRedirect('/crop/list/')
        connection.commit()
    else:
        return HttpResponse('You have in get method')
    
def croplist(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM crops")
    id=request.session.get('admin_id')
    settings=Settings.objects.filter(id='1')
    myresult = cursor.fetchall()
    admin=Admin.objects.filter(id=id)
    data={
        'abc':myresult,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/crop/croplist.html',data)

# ==================crop section end==============================

# ==================Product Section Start===========================

def addproduct(request):
    roles=Roles.objects.all()
    users=Users.objects.all()
    crops=Crops.objects.all()
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        'role':roles,
        'user':users,
        'crop':crops,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/product/addproduct.html',data)

def productsave(request):
    if request.method=="POST":
        # now = datetime.now()
        current_datetime = datetime.datetime.now()
        cursor = connection.cursor()
        name=request.POST.get('name')
        price=request.POST.get('price')
        cropid=request.POST.get('crop')
        userid=request.POST.get('user')
        roleid=request.POST.get('role')
        quality=request.POST.get('quality')
        image=request.FILES['image']
        
        # sql = """INSERT INTO user(name, email, mobile, password, aadharno,fathername,status)VALUES ('name', 'email', 'password', 'mobile', 'aadharno','fathername','1')"""
        # add_user = ("INSERT INTO users "
        #         "(name, userid, cropid, price, quality,roleid,status,image) "
        #         "VALUES (%s, %s, %s, %s, %s, %s,%s,%s)")

        # data_user = (name, userid, cropid, price, quality,roleid,1,image)
        prod=Product(name=name,userid=userid,cropid=cropid,price=price,quality=quality,roleid=roleid,status='1',image=image,datetime=current_datetime)
        prod.save()
        return HttpResponseRedirect('/product/list/')
    else:
        return HttpResponse('You are in get method')

def productlist(request):
    if request.method=="GET":
        cursor = connection.cursor()
        
        c="SELECT product.*,crops.name AS cropname,users.name AS username,roles.name AS rolename FROM `product`,`users`,`roles`,`crops` WHERE product.userid=users.id&&product.cropid=crops.id&&product.roleid=roles.id"
        id=request.session.get('admin_id')
        settings=Settings.objects.filter(id='1')
        ac=cursor.execute(c)
        myresult = cursor.fetchall()
        admin=Admin.objects.filter(id=id)
        if ac==():
            return HttpResponse('Error')
        else:
            data={
                'abc':myresult,
                'admindata':admin,
                'adminsettings':settings,
            }
            return render(request,'enroll/product/productlist.html',data)
        connection.commit()
    else:
        return HttpResponse('You have in get method')
# ===================Product Section End============================
    
# ===================Role Section Start =============================
def addrole(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    
    settings=Settings.objects.filter(id='1')
    data={
            'admindata':admin,
            'adminsettings':settings,
        }
    return render(request,'enroll/role/addrole.html',data)

def rolesave(request):
    if request.method=="POST":
        # now = datetime.now()
        current_datetime = datetime.datetime.now()
        cursor = connection.cursor()
        Name=request.POST.get('name')
        print(Name)
        # image=request.FILES['image']
        prod=Roles(name=Name,status='1')
        prod.save()
        return HttpResponseRedirect('/role/list/')
    else:
        return HttpResponse('You are in get method')

def listrole(request):
    id=request.session.get('admin_id')
    roles=Roles.objects.all()
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        'abc':roles,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/role/rolelist.html',data)
# ===================Role Section End ==============================

# ===================Page Start=====================================
def privacy(request):
    id=request.session.get('admin_id')
    member = privacypolicy.objects.filter(id=1)
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        "abc":member,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/page/privacypolicy.html',data)

def updateprivacy(request):
    privacy=request.POST.get('privacy')
    member = privacypolicy.objects.get(id=1)
    member.privacy = privacy
    member.save()
    return HttpResponseRedirect('/privacy/view/')

def terms(request):
    id=request.session.get('admin_id')
    member = Termcondition.objects.filter(id=1)
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        "abc":member,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/page/term_condition.html',data)

def updateterms(request):
    terms=request.POST.get('terms')
    member = Termcondition.objects.get(id=1)
    member.terms = terms
    member.save()
    return HttpResponseRedirect('/terms/view/')

def aboutus(request):
    id=request.session.get('admin_id')
    member = AboutUs.objects.filter(id=1)
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    data={
        "abc":member,
        'admindata':admin,
        'adminsettings':settings,
    }
    return render(request,'enroll/page/about_us.html',data)

def updateaboutus(request):
    terms=request.POST.get('terms')
    member = AboutUs.objects.get(id=1)
    member.terms = terms
    member.save()
    return HttpResponseRedirect('/about/view/')
# ===================Page End=======================================
    
def dtata(request):
    member = Termcondition.objects.filter(id=1)
    for n in member:
        n.terms
    terms=n.terms
    print(html.unescape(terms)) 
    tr=html.unescape(terms)
    s = html.escape( """<p><strong>HealthCRAD Privacy Policy</strong><br /> This Privacy Policy governs how we,“HealthCRAD” ,“Company”,“we”,“us” or"our”) collect, use, share and process your information, that you provide to us through your use of the app, HealthCRAD and Website www.apollopharmacy.in in the course of providing services(“Services”) as defined in the Terms and Conditions terms to you.</p>""" )
    print(s)
    data={
        "abc":s
    }
    
    return render(request,'enroll/userregister.html',data)

# ==========================Start Offer Details==============================
def offerdetails(request, ids):
    idss=str(ids)
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    users=Users.objects.get(id=idss)
    usermobile=users.mobile
    username=users.name
    role=users.roll_id
    cursor = connection.cursor()
    cursor.execute("SELECT offers_farmer.*,product.name AS productname FROM offers_farmer,product WHERE offers_farmer.productid=product.id && offers_farmer.farmer_id="+idss)
    # print("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.roll_id="+role)
    farmoffer = cursor.fetchall()
    if role=='1':
        farmeroffer=farmeroffers.objects.filter(farmer_id=ids)
        print(farmeroffer)
        if farmeroffer:
            farmeroffer=farmeroffers.objects.get(farmer_id=ids)
            status=farmeroffer.offerstatus
            if status == '0':
                statusdata='Pending'
            else:
                statusdata='Success'
            data={
                "abc":farmoffer,
                'admindata':admin,
                'adminsettings':settings,
                'statusdata':statusdata,
                'username':username,
                'usermobile':usermobile
            }
        else:
            data={
                'admindata':admin,
                'adminsettings':settings,
                'username':username,
                'usermobile':usermobile
            }
        return render(request,'enroll/offerdetails/farmer.html',data)
    elif role=='2':
        cursor.execute("SELECT offers_buyer.*,product.name AS productname FROM offers_buyer,product WHERE offers_buyer.productid=product.id && offers_buyer.buyer_id="+idss)
        # print("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.roll_id="+role)
        buyoffer = cursor.fetchall()
        buyeroffer=buyeroffers.objects.filter(buyer_id=ids)
        print(buyeroffer)
        if buyeroffer:
            buyeroffer=buyeroffers.objects.get(buyer_id=ids)
            status=buyeroffer.offerstatus
            if status == '0':
                statusdata='Pending'
            else:
                statusdata='Success'
            data={
                "abc":buyoffer,
                'admindata':admin,
                'adminsettings':settings,
                'statusdata':statusdata,
                'username':username,
                'usermobile':usermobile
            }
        else:
            data={
                'admindata':admin,
                'adminsettings':settings,
                'username':username,
                'usermobile':usermobile
            }
        return render(request,'enroll/offerdetails/buyer.html',data)
    else:
        cursor.execute("SELECT offers_logistics.* FROM offers_logistics WHERE offers_logistics.logistics_id="+idss)
        # print("SELECT users.*,roles.name AS rolename FROM users,roles WHERE users.roll_id=roles.id && users.roll_id="+role)
        logioffer = cursor.fetchall()
        logisticsoffer=Logisticsoffers.objects.filter(logistics_id=ids)
        # print(buyeroffer)
        if logisticsoffer:
            logisticsoffer=Logisticsoffers.objects.get(logistics_id=ids)
            status=logisticsoffer.offerstatus
            if status == '0':
                statusdata='Pending'
            else:
                statusdata='Success'
            data={
                "abc":logioffer,
                'admindata':admin,
                'adminsettings':settings,
                'statusdata':statusdata,
                'username':username,
                'usermobile':usermobile
            }
        else:
            data={
                'admindata':admin,
                'adminsettings':settings,
                'username':username,
                'usermobile':usermobile
            }
        return render(request,'enroll/offerdetails/logistics.html',data)
    
#  =========================End Offer Details==========================
# ==========================Start Transaction Details==================
def farmpayment(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    trans=Transactions.objects.all()
    for n in trans:
        fid=n.farmer_id
        bid=n.buyer_id
        lid=n.logistics_id
        cropid=n.cropid
        print(lid)
        farmd=Users.objects.filter(id=fid)
        cropd=Product.objects.filter(id=cropid)
        print(cropd.query)
        for f in farmd:
            farmname=f.name
            print("Farmer Name:" ,farmname)
            buyerd=Users.objects.filter(id=bid)
            # print(Users.objects.filter(id=bid).query)
            for b in buyerd:
                buyername=b.name
                print("Buyer Name:" ,buyername)
                logisd=Users.objects.filter(id=lid)
                # print(Users.objects.filter(id=bid).query)
                for l in logisd:
                    loginame=l.name
                    print("Logistics Name:" ,loginame)
                    print("=====================")
                    for c in cropd:
                        cropname=c.name
                        print("crop name:",cropname)
                        data={
                            'admindata':admin,
                            'adminsettings':settings,
                            'trasaction':trans,
                            'farmername':farmname,
                            'buyername':buyername,
                            'cropname':cropname,
                            'logisticsname':loginame
                        }
                        print('########################################')
                        print(data)
                        print('########################################')
    
    return render(request,'enroll/transactions/farmer.html',data)

def logistics(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    trans=Transactions.objects.all()
    for n in trans:
        fid=n.farmer_id
        bid=n.buyer_id
        lid=n.logistics_id
        cropid=n.cropid
        print(lid)
        farmd=Users.objects.filter(id=fid)
        cropd=Product.objects.filter(id=cropid)
        print(cropd.query)
        for f in farmd:
            farmname=f.name
            print("Farmer Name:" ,farmname)
            buyerd=Users.objects.filter(id=bid)
            # print(Users.objects.filter(id=bid).query)
            for b in buyerd:
                buyername=b.name
                print("Buyer Name:" ,buyername)
                logisd=Users.objects.filter(id=lid)
                # print(Users.objects.filter(id=bid).query)
                for l in logisd:
                    loginame=l.name
                    print("Logistics Name:" ,loginame)
                    print("=====================")
                    for c in cropd:
                        cropname=c.name
                        print("crop name:",cropname)
                        data={
                            'admindata':admin,
                            'adminsettings':settings,
                            'trasaction':trans,
                            'logistics':loginame,
                            'buyername':buyername,
                            'cropname':cropname
                        }
                        print(data)
    
    return render(request,'enroll/transactions/logistics.html',data)
# ==========================End Transaction Details=====================
# ==========================Start Field Issues==========================
def farmerfield(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settings=Settings.objects.filter(id='1')
    cursor = connection.cursor()
    cursor.execute("SELECT fieldissue.*,users.name AS username,users.mobile AS usermobile FROM fieldissue,users WHERE fieldissue.farmerid=users.id")
    
    myresult = cursor.fetchall()
    data={
        'admindata':admin,
        'adminsettings':settings,
        'farmfield':myresult
    }
    print(data)
    
    return render(request,'enroll/fieldissues/index.html',data)
def getaddressbymap(request, id):
    
    FieldIssues=FieldIssue.objects.get(id=id)
    address=FieldIssues.location
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(address)
    latitude=location.latitude
    longitude=location.longitude
    print("The latitude of the location is: ", latitude)
    print("The longitude of the location is: ", longitude)
    data={
        'map':FieldIssues,
        'latitude':latitude,
        'longitude':longitude
    }
    print(data)
    
    return render(request,'enroll/fieldissues/map.html',data)
# ==========================End Field Issues============================
# ==========================Start Settings==============================
def adsettings(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settingss=Settings.objects.filter(id='1')
    data={
        'admindata':admin,
        'adminsettings':settingss,
    }
    print(data)
    
    return render(request,'enroll/page/settings.html',data)
# ==========================End Settings================================
# ==========================Start Settings==============================
def adsettings(request):
    id=request.session.get('admin_id')
    admin=Admin.objects.filter(id=id)
    settingss=Settings.objects.filter(id='1')
    data={
        'admindata':admin,
        'adminsettings':settingss,
    }
    print(data)
    
    return render(request,'enroll/page/settings.html',data)

def updateadsettings(request):
    if request.method=="POST":
        # now = datetime.now()
        current_datetime = datetime.datetime.now()
        cursor = connection.cursor()
        compname=request.POST.get('compname')
        compemail=request.POST.get('compemail')
        compphone=request.POST.get('compphone')
        compadd=request.POST.get('compadd')
        copyright=request.POST.get('copyright')
        
        if 'image' in request.FILES:
            company_logo=request.FILES['image']
            settingss=Settings.objects.filter(id='1')
            for object in settingss:
            # object.save()
                object.company_name = compname
                object.company_email = compemail
                object.company_mobile = compphone
                object.shopaddress = compadd
                object.copyright = copyright
                object.company_logo = company_logo
                object.company_favicon = company_logo
                object.save()
            return HttpResponseRedirect('/view/settings')
        else:
            settingss=Settings.objects.filter(id='1')
            for object in settingss:
            # object.save()
                object.company_name = compname
                object.company_email = compemail
                object.company_mobile = compphone
                object.shopaddress = compadd
                object.copyright = copyright
                object.save()
            # print(object.query)
            return HttpResponseRedirect('/view/settings')
# ==========================End Settings================================
# ===========================Start Get Lat Long by address==============
def address(request):
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode("yusufpur")

    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
# ==========================End Get Lat Long by address==================