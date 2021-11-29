from django.core.exceptions import FieldDoesNotExist
from auth_mercagro.models.account   import Account
from auth_mercagro.models.user      import User
from .accountSerializer             import Account
from rest_framework                 import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model   = User
        fields  = ['id','username','password','name','email', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
    
    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        account = Account.objets.get(user=obj.id)
        return{
            'id'        : user.id,
            'username'  : user.username,
            'name'      : user.name,
            'email'     : user.email,
            'account'   :{
                'id'            : account.id,
                'balance'       : account.balance,
                'lastChangeData': account.lastChangeData,
                'isActivate'    : account.isActivate,
            }
        }