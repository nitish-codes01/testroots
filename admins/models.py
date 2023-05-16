from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250,null=True,default=None)
    email=models.EmailField(max_length=250,null=True,default=None)
    password=models.CharField(max_length=250,null=True,default=None)
    mobile=models.CharField(max_length=250,null=True,default=None)
    fathername=models.CharField(max_length=250,null=True,default=None)
    aadharno=models.CharField(max_length=250,null=True,default=None)
    roll_id=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)
    image=models.FileField(upload_to="user/",max_length=500,null=True,default=None)
    accountno=models.CharField(max_length=250,null=True,default=None)
    bankname=models.CharField(max_length=250,null=True,default=None)
    branchname=models.CharField(max_length=250,null=True,default=None)
    ifsc=models.CharField(max_length=250,null=True,default=None)
    class Meta:
        db_table='users'

class Roles(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250,null=True,default=None)
    slug=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='roles'

class Account(models.Model):
    id=models.AutoField(primary_key=True)
    holdername=models.CharField(max_length=250,null=True,default=None)
    accountnumber=models.CharField(max_length=250,null=True,default=None)
    branch=models.CharField(max_length=250,null=True,default=None)
    ifsc=models.CharField(max_length=250,null=True,default=None)
    bank_name=models.CharField(max_length=250,null=True,default=None)
    user_id=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='accounts'

class Notifications(models.Model):
    id=models.AutoField(primary_key=True)
    roleid=models.CharField(max_length=250,null=True,default=None)
    userid=models.CharField(max_length=250,null=True,default=None)
    productid=models.CharField(max_length=250,null=True,default=None)
    datetime=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class meta:
        db_table='notification'

class Transactionhistory(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.CharField(max_length=250,null=True,default=None)
    productid=models.CharField(max_length=250,null=True,default=None)
    amount=models.CharField(max_length=250,null=True,default=None)
    datetime=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class meta:
        db_table='transaction_history'

class Qualityparam(models.Model):
    id=models.AutoField(primary_key=True)
    certificat_id=models.CharField(max_length=250,null=True,default=None)
    location=models.CharField(max_length=250,null=True,default=None)
    image=models.CharField(max_length=250,null=True,default=None)
    cropid=models.CharField(max_length=250,null=True,default=None)
    testid=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class meta:
        db_table='quality_parameter'

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=250,null=True,default=None)
    email=models.CharField(max_length=250,null=True,default=None)
    password=models.CharField(max_length=250,null=True,default=None)
    phone=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)
    image=models.FileField(upload_to="profile/",max_length=500,null=True,default=None)
    class Meta:
        db_table='admin'

class Crops(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250,null=True,default=None)
    image=models.FileField(upload_to="crop/",max_length=500,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='crops'

class Auction(models.Model):
    id=models.AutoField(primary_key=True)
    fid=models.CharField(max_length=250,null=True,default=None)
    productid=models.CharField(max_length=250,null=True,default=None)
    userid=models.CharField(max_length=250,null=True,default=None)
    datetime=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='auctions'

class Quaitytestuser(models.Model):
    id=models.AutoField(primary_key=True)
    # role=models.ForeignKey(Roles,on_delete=models.CASCADE,null=True,related_name='roles')
    farmer=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,related_name='farmers')
    # farmerid=models.CharField(max_length=250,null=True,default=None)
    location=models.CharField(max_length=250,null=True,default=None)
    images=models.FileField(upload_to="fieldissue/",max_length=500,null=True,default=None)
    multipleimages=models.FileField(upload_to="fieldissue/multi",max_length=500,null=True,default=None)
    Certificateid=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)
    certificateimage=models.FileField(upload_to="fieldissue/certificate",max_length=500,null=True,default=None)

    class Meta:
        db_table='qualitytestuser'

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.CharField(max_length=250,null=True,default=None)
    cropid=models.CharField(max_length=250,null=True,default=None)
    name=models.CharField(max_length=250,null=True,default=None)
    price=models.CharField(max_length=250,null=True,default=None)
    quality=models.CharField(max_length=250,null=True,default=None)
    location=models.CharField(max_length=250,null=True,default=None)
    image=models.FileField(upload_to="product/",max_length=500,null=True,default=None)
    datetime=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)
    # roleid=models.ForeignKey(Roles,on_delete=models.CASCADE,null=True,related_name='roles')
    roleid=models.CharField(max_length=250,null=True,default=None)
    discount=models.CharField(max_length=250,null=True,default=None)
    stoct=models.CharField(max_length=250,null=True,default=None)
    is_discount=models.CharField(max_length=250,null=True,default=None)
    discounted_price=models.CharField(max_length=250,null=True,default=None)
    class Meta:
        db_table='product'

class Settings(models.Model):
    id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=250,null=True,default=None)
    company_logo=models.FileField(upload_to="settings/logo/",max_length=500,null=True,default=None)
    company_email=models.CharField(max_length=250,null=True,default=None)
    company_mobile=models.CharField(max_length=250,null=True,default=None)
    copyright=models.CharField(max_length=250,null=True,default=None)
    shopaddress=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)
    company_favicon=models.FileField(upload_to="settings/favicon/",max_length=500,null=True,default=None)
    class Meta:
        db_table='settings'

class privacypolicy(models.Model):
    id=models.AutoField(primary_key=True)
    privacy=models.CharField(max_length=15000,null=True,default=None)
    class Meta:
        db_table='privacy_policy'

class Termcondition(models.Model):
    id=models.AutoField(primary_key=True)
    terms=models.CharField(max_length=16000,null=True,default=None)
    class Meta:
        db_table='term_condition'

class AboutUs(models.Model):
    id=models.AutoField(primary_key=True)
    about=models.CharField(max_length=16200,null=True,default=None)
    class Meta:
        db_table='aboutus'

class Order_details(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.CharField(max_length=250,null=True,default=None)
    product_id=models.CharField(max_length=250,null=True,default=None)
    seller_id=models.CharField(max_length=250,null=True,default=None)
    qty=models.CharField(max_length=250,null=True,default=None)
    price=models.CharField(max_length=250,null=True,default=None)
    discount=models.CharField(max_length=250,null=True,default=None)
    tax=models.CharField(max_length=250,null=True,default=None)
    delivery_status=models.CharField(max_length=250,null=True,default=None)
    datetime=models.CharField(max_length=250,null=True,default=None)
    class Meta:
        db_table='order_details'
    
class farmeroffers(models.Model):
    id=models.AutoField(primary_key=True)
    offerdate=models.CharField(max_length=250,null=True,default=None)
    # productid=models.CharField(max_length=250,null=True,default=None)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='roles')
    # productid=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='farmeroffers')
    quantity=models.CharField(max_length=250,null=True,default=None)
    price=models.CharField(max_length=250,null=True,default=None)
    totalamount=models.CharField(max_length=250,null=True,default=None)
    pickuplocation=models.CharField(max_length=250,null=True,default=None)
    # delivery_location=models.CharField(max_length=250,null=True,default=None)
    offerstatus=models.CharField(max_length=250,null=True,default=None)
    farmer_id=models.CharField(max_length=250,null=True,default=None)
    # buyer_id=models.CharField(max_length=250,null=True,default=None)
    # loistics_id=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='offers_farmer'


class buyeroffers(models.Model):
    id=models.AutoField(primary_key=True)
    offerdate=models.CharField(max_length=250,null=True,default=None)
    # productid=models.CharField(max_length=250,null=True,default=None)
    quantity=models.CharField(max_length=250,null=True,default=None)
    price=models.CharField(max_length=250,null=True,default=None)
    bidamount=models.CharField(max_length=250,null=True,default=None)
    # pickuplocation=models.CharField(max_length=250,null=True,default=None)
    delivery_location=models.CharField(max_length=250,null=True,default=None)
    offerstatus=models.CharField(max_length=250,null=True,default=None)
    # farmoffer_id=models.CharField(max_length=250,null=True,default=None)
    buyer_id=models.CharField(max_length=250,null=True,default=None)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='products')
    # loistics_id=models.Charq2111111`Field(max_length=250,null=True,default=None)

    class Meta:
        db_table='offers_buyer'

class Logisticsoffers(models.Model):
    id=models.AutoField(primary_key=True)
    offerdate=models.CharField(max_length=250,null=True,default=None)
    traveldate=models.CharField(max_length=250,null=True,default=None)
    price=models.CharField(max_length=250,null=True,default=None)
    source_location=models.CharField(max_length=250,null=True,default=None)
    destination_location=models.CharField(max_length=250,null=True,default=None)
    offerstatus=models.CharField(max_length=250,null=True,default=None)
    farmoffer_id=models.CharField(max_length=250,null=True,default=None)
    logistics_id=models.CharField(max_length=250,null=True,default=None)
    quantity=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='offers_logistics'

class Transactions(models.Model):
    id=models.AutoField(primary_key=True)
    treasactiondate=models.CharField(max_length=250,null=True,default=None)
    transaction_id=models.CharField(max_length=250,null=True,default=None)
    cropid=models.CharField(max_length=250,null=True,default=None)
    farmer_id=models.CharField(max_length=250,null=True,default=None)
    farmer_amount=models.CharField(max_length=250,null=True,default=None)
    buyer_id=models.CharField(max_length=250,null=True,default=None)
    buyer_amount=models.CharField(max_length=250,null=True,default=None)
    logistics_id=models.CharField(max_length=250,null=True,default=None)
    logistics_amount=models.CharField(max_length=250,null=True,default=None)
    status=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='transactions'

class FieldIssue(models.Model):
    id=models.AutoField(primary_key=True)
    farmerid=models.CharField(max_length=250,null=True,default=None)
    location=models.CharField(max_length=250,null=True,default=None)
    images=models.FileField(upload_to="fieldissue/",max_length=500,null=True,default=None)

    class Meta:
        db_table='fieldissue'

class abcd(models.Model):
    id=models.AutoField(primary_key=True)
    productid=models.ForeignKey(Roles,on_delete=models.CASCADE,null=True,related_name='product')
    name=models.CharField(max_length=250,null=True,default=None)

    class Meta:
        db_table='demoabcd'
