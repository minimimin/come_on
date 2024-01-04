from django.db import models

# Create your models here.

# django.db.models 모듈에 Model이라는 부모 클래스 상속 이라는 뜻
# Model이라는 부모클래스에는 model에 관련된 모든 코드가 이미 작성되어 있음
# 이게 바로 프레임워크의 장점! 다 코드가 짜져있으니까 중요 테이블 구조를 어떻게 설계할지만 생각하면 된다.

class Article(models.Model):
    # 모델 클래스 만들고
    # 아래에 DB 테이블에 저장될 명칭과 제약조건, 입력 데이터 타입을 적어주기
    # 필드 명칭 = models.입력할 데이터 타입(제약조건) 형식
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 처음 생성될 때 기준으로만 시간 저장
    updated_at = models.DateTimeField(auto_now=True)

# 모델에 저장한 후 DB에 migration 해주는 거 잊지마!!
# bash에 
# python manage.py makemigrations
# python manage.py migrate
# 입력하기

# migration 되었는 지 확인하려면 
# python manage.py showmigrations 해서 확인하기
# X라고 되어있으면 migrate 완료된 것!

# 그 다음은 admin.py에 모델클래스 등록해서 admin사이트에서 볼 수 있도록 하기!
