from rest_framework import serializers
from admins.models import Users,Roles,Product,farmeroffers,buyeroffers,abcd,Quaitytestuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class farmofferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source="productid")
    class Meta:
        model=farmeroffers
        fields="__all__"

class buyerofferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source="productsid")
    class Meta:
        model=buyeroffers
        fields="__all__"

class AbcSerializer(serializers.ModelSerializer):
    model_b = RoleSerializer(source="productid")
    class Meta:
        model=abcd
        fields="__all__"
#          fields = ("offerdate", "quantity", "price", "pickuplocation","offerstatus","farmer_id","totalamount")

class certificatesSerializer(serializers.ModelSerializer):
    User = UserSerializer(source="farmer")
    class Meta:
        model=Quaitytestuser
        # fields=["Certificateid", "location", "status", "certificateimage","farmer_id","images","multipleimages"]
        fields="__all__"