-- PRICE의 최고값 구한다음, 거기까지 범위를 설정해야함.
-- 위를 대신 할 수 있는 게 PARTITION BY OVER 어쩌고 그거 쓰는 거 같은데,,흠
WITH
    PRICE_LIST AS (
        SELECT 
            FLOOR(PRICE / 10000)*10000 AS PRICE_GROUP
        FROM PRODUCT
    )

-- 만원 단위 가격대 별(최소금액으로 표시)로 상품 개수 출력
SELECT PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRICE_LIST
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP