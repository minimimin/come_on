-- 코드를 입력하세요
# 실행순서 : FROM (+ JOIN) - WHERE - GROUP BY - HAVING - SELECT - ORDER BY - LIMIT
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
# MAX(FAVORITES)를 먼저 실행해야하기에
# 서브쿼리 작성하기
# GROUP BY로 묶으면 가장 상단에 있는 데이터들을 임의로 가져온다.
# SELECT에 MAX를 해도 최대값을 가져오는것이 아닌 그룹화된 테이블 가장 상단을 가져오게 된다.
FROM REST_INFO
WHERE (FAVORITES, FOOD_TYPE) IN (SELECT MAX(FAVORITES), FOOD_TYPE FROM REST_INFO GROUP BY FOOD_TYPE)
# 서브쿼리에서 GROUP BY로 FOOD_TYPE별로 나오니까 구하는 것도 FOOD_TYPE여야한다!
# GROUP BY FOOD_TYPE
# HAVING MAX(FAVORITES)
# 서브쿼리에서 이미 그룹화했기때문에 따로 해줄필요 없다!
ORDER BY FOOD_TYPE DESC