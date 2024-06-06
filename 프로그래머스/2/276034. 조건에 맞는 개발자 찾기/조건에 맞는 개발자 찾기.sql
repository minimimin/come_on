# SELECT ID, EMAIL, LAST_NAME, FIRST_NAME
# FROM DEVELOPERS
# WHERE SKILL_CODE IN (
#     SELECT CODE
#     FROM SKILLCODES
#     WHERE NAME = 'Python' OR NAME = 'C#'
# )

SELECT distinct D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D, SKILLCODES S
WHERE (D.SKILL_CODE & S.CODE) > 0
    AND (S.NAME = 'Python' OR S.NAME = 'C#')
ORDER BY D.ID