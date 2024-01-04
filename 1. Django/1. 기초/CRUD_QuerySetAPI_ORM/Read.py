# 데이터 조회
# Articles 모델이 있다고 치고 함

# 1.
# 전체 데이터 조회
Articles.objects.all()
# 모델의 모든 행들을 불러와! 보여줘! 이런 뜻

# 2.
# 단일 데이터 조회
Articles.objects.get(pk=1)
Articles.objects.get(content='content')
# 모델에서 해당 조건에 해당하는 것들이 조회되도록 하는 것!
# 객체 찾을 수 없거나 둘 이상의 객체를 찾게 될 경우 예외가 뜬다
# 그래서 보통 pk(primary key)를 통해 조회하게 된다.


# 3. 
# 특정 조건 데이터 조회
Articles.objects.filter(content='content')
# 단일 데이터 조회와 다르게 객체를 찾을 수 없거나 둘 이상의 객체를 찾아도 오류가 나지 않음
# 아무것도 없으면 아무것도 없다고 빈 리스트 반환, 둘 이상의 객체를 찾으면 둘 이상의 객체를 찾아서 반환
# 리스트로 반환

Articles.objects.filter(content__contains='con')
# content 컬럼에 'con'이 포함된 모든 데이터 조회하는 것!
