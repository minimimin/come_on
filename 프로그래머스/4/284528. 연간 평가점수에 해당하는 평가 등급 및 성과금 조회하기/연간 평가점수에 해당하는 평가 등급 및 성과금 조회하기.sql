-- 사원별 성과금 정보 조회(사번, 성명, 평가등급, 성과금)
-- HR_DEPARTMENT는 사용 안 함
-- HR_EMPLOYEES에서 EMP_NO, EMP_NAME, SAL(성과금 계산용)
-- HR_GRADE에서 EMP_NO, SCORE
-- SCORE에 따라 평가등급이랑 성과금 나눠진다.
WITH GRADE_CASE AS(
    SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT E.EMP_NO, E.EMP_NAME, G.GRADE,
    CASE
        WHEN G.GRADE = 'S' THEN E.SAL*0.2
        WHEN G.GRADE = 'A' THEN E.SAL*0.15
        WHEN G.GRADE = 'B' THEN E.SAL*0.1
        ELSE 0
    END AS BONUS
FROM HR_EMPLOYEES E
JOIN GRADE_CASE G
ON E.EMP_NO = G.EMP_NO
ORDER BY E.EMP_NO