from django import forms
from .models import *
class LoginForm(forms.ModelForm):
    class Meta:
        #属性1:uphone
        #属性2:upwd
        #1.指定关联的实体类
        model = Users
        #2.指定取出哪些字段生成控件
        fields = ['uphone','upwd']
        #3.指定每个控件的label
        labels = {
            'uphone' : '手机号',
            'upwd' : '密码',
        }
        #4.指定每个控件的小部件
        widgets = {
            'uphone':forms.TextInput(
                attrs = {
                    'class' : 'uinput',
                }
            ),
            'upwd' : forms.PasswordInput(
                attrs = {
                    'class' : 'uinput',
                    'placeholder':'请输入6-20位的号码字符',
                }
            )
        }
