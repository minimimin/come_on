SELECT I.INGREDIENT_TYPE, SUM(O.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF O, ICECREAM_INFO I
WHERE O.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY SUM(O.TOTAL_ORDER)