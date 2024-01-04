from django.contrib import admin
# 만들어 놓은 모델클래스 불러오기!
from .models import Article

# Register your models here.
# 어드민 사이트에 등록해라 (모델클래스를)
admin.site.register(Article)

# 이거 확인하려면 admin 관리자 계정 만들어주기!
# python manage.py createsuperuser