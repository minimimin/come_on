SELECT F.FLAVOR
FROM FIRST_HALF F
    FULL OUTER JOIN JULY J
    ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
FETCH FIRST 3 ROWS ONLY