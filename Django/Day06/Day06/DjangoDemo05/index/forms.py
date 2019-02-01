from django import forms
from .models import *

#为level控件初始化数据
LEVEL_CHOICE=(
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)

#表示评论内容的表单控件们
#控件1 - 评论标题(subject) - 文本框
#控件2 - Email(email) - Email框
#控件3 - 评论内容(message) - Textarea
#控件4 - 评论级别(level) - Select
#控件5 - 是否保存(isSaved) - Checkbox
class RemarkForm(forms.Form):
    # 控件1 - 评论标题(subject) - 文本框
    # label : 表示控件前的标签文本
    subject=forms.CharField(label='标题')
    # 控件2 - Email(email) - Email框
    email = forms.EmailField(label='邮箱')
    # 控件3 - 评论内容(message) - Textarea
    # widget=forms.Textarea　为了将控件变为多行文本域
    message = forms.CharField(
        label='内容',
        widget=forms.Textarea
    )
    # 控件4 - 评论级别(level) - Select
    level = forms.ChoiceField(
        label='级别',
        choices=LEVEL_CHOICE
    )
    # 控件5 - 是否保存(isSaved) - Checkbox
    isSaved = forms.BooleanField(
        label='是否保存'
    )

class RegisterForm(forms.Form):
    uname=forms.CharField(label='用户名称')
    upwd=forms.CharField(label='用户密码')
    uage=forms.IntegerField(label='用户年龄')
    uemail=forms.EmailField(label='电子邮箱')

class ModelRegisterForm(forms.ModelForm):
    class Meta:
        #1.指定关联的Model类 - model
        model = Users
        #2.指定要生成控件的字段们 - fields
        fields = "__all__"
        #3.指定每个属性对应的label - labels
        labels = {
            'uname':'用户名称',
            'upwd':'用户密码',
            'uage':'用户年龄',
            'uemail':'电子邮件'
        }

class ModelLoginForm(forms.ModelForm):
    class Meta:
        #1.指定关联实体类-model
        model = Users
        #2.指定要生成控件的字段们-fields
        fields = ["uname","upwd"]
        #3.指定属性所对应的label-labels
        labels = {
            'uname' : '登录名称',
            'upwd' : '登录密码',
        }

class WidgetRegisterForm(forms.Form):
    #用户名称-type=text
    uname = forms.CharField(
        label='用户名称',
        widget=forms.TextInput(
            attrs = {
                'placeholder' : '请输入用户名',
                'class' : 'form-control'
            }
        )
    )
    #用户密码-type=password
    upwd = forms.CharField(
        label='用户密码',
        widget=forms.PasswordInput(
            attrs = {
                'placeholder':'请输入密码',
                'class':'form-control',
            }
        )
    )
    #评论级别-type=radio
    level = forms.ChoiceField(
        label='评论级别',
        choices=LEVEL_CHOICE,
        widget=forms.RadioSelect
    )







