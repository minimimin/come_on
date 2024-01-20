-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME) AS count
# DISTINCT는 같은 값이면 중복을 제거한다는 뜻!!
# 옆에 온 모든 컬럼을 고려하여 중복 제거를 진행
# = DISTINCT 는 SELECT 구문에 여러 컬럼명이 올 때, 그 중 한 개에 대해서만 적용할 수 없다는 뜻!
FROM ANIMAL_INS
WHERE NAME IS NOT NULL