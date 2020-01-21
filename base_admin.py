from django.contrib import admin
from django.contrib.admin.models import LogEntry

from custom_site import custom_site


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.用来自动补充文章，分类，标签，侧边栏，友链这些Model的owner字段
    2.用来对queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    # 仅显示自己编辑的文章
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

