-- 코드를 입력하세요
SELECT B.USER_ID, B.NICKNAME, SUM(A.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD A
# , USED_GOODS_USER B
    INNER JOIN USED_GOODS_USER B
    ON A.WRITER_ID = B.USER_ID
WHERE STATUS = 'DONE'
    # AND SUM(A.PRICE) > 700000
# 회원별로 찾아서 금액을 다 더해야하는 거 같은데..흠..회원id가 같은 것들끼리 다 더해라..!
GROUP BY B.USER_ID
HAVING SUM(A.PRICE) >= 700000
ORDER BY SUM(A.PRICE)