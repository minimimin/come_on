-- 코드를 입력하세요
SELECT A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, sum(A.PRICE*C.SALES) AS TOTAL_SALES
FROM BOOK A
    INNER JOIN AUTHOR B
    ON A.AUTHOR_ID = B.AUTHOR_ID
    INNER JOIN BOOK_SALES C
    ON A.BOOK_ID = C.BOOK_ID
WHERE C.SALES_DATE LIKE '2022-01-%'
GROUP BY B.AUTHOR_ID, A.CATEGORY
ORDER BY B.AUTHOR_ID, A.CATEGORY DESC