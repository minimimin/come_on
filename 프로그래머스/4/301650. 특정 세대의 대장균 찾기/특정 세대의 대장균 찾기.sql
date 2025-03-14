# SELECT ID
# FROM ECOLI_DATA
# WHERE PARENT_ID IN (
#     SELECT ID
#     FROM ECOLI_DATA
#     WHERE PARENT_ID IN (
#         SELECT ID
#         FROM ECOLI_DATA
#         WHERE PARENT_ID IS NULL
#     ))
# ORDER BY ID

SELECT CC.ID
FROM ECOLI_DATA CC
    JOIN ECOLI_DATA C
    ON CC.PARENT_ID = C.ID
    JOIN ECOLI_DATA P
    ON C.PARENT_ID = P.ID
WHERE P.PARENT_ID IS NULL
ORDER BY ID