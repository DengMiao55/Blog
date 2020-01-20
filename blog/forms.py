from django import forms

# from .models import Student
#
# class StudentForm(forms.ModelForm):
#     # name = forms.CharField(label='姓名', max_length=128)
#     # sex = forms.IntegerField(choices=Student.SEX_ITEMS, verbose_name="性别")
#     # profession = forms.CharField(max_length=128, verbose_name="职业")
#     # email = forms.EmailField(verbose_name="邮箱")
#     # qq = forms.CharField(max_length=128, verbose_name="QQ")
#     # phone = forms.CharField(max_length=128, verbose_name="电话")
#
#     def clean_qq(self):
#         cleaned_data = self.cleaned_data['qq']
#         if not cleaned_data.isdigit():
#             raise forms.ValidationError({"必须是数字！"})
#         return int(cleaned_data)
#
#     class Meta:
#         model = Student
#         fields = (
#             'name', 'sex', 'profession',
#             'email', 'qq', 'phone'
#         )