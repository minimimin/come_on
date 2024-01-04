# 데이터 삭제
# delete 메서드 사용하기
# 조회 후 삭제하면 끝

# 예)
article = Articles.objects.get(pk=1)
article.delete()