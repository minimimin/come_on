# 데이터 객체 생성 방법

# Articles 모델(그 안에 title, content, created_at이 있다)이 있다고 치고 함
# Datetimefield(auto_now=True)는 자동으로 작성될거라서 따로 값 안넣어줘도 된다 
# 특정 테이블에 새로운 행을 추가하여 데이터 추가
# 모델 클래스로부터 인스턴스 생성하기


# 1.
article = Articles()
article.title = 'title'
article.content = 'content'
# 인스턴스 변수에 값을 넣어준다(DB에 넣어주기 위해)
article.save()
# ★ 무조건 저장해주기! 만들고나서 저장안하면 없는 거


# 2.
article = Article(title='title', content='content')
article.save()
# 1번의 3줄을 1줄로 만들어 준 것!


# 3.
# ★ QuerySet API의 create() 메서드 활용하기
# save() 필요 없어!
Article.objects.create(title='title', content='content')