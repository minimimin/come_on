# 조회 후 변경하고 저장하면
# 그게 바로 데이터 수정!

# 예)
article = Articles.objects.get(pk=1)
article.title = 'change'
article.save()