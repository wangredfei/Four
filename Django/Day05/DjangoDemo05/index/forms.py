from django import forms

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




