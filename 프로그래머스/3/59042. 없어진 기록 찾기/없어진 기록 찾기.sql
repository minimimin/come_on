-- 입양 간 기록(나간 기록)은 있는데 들어온 기록이 없는 동물 조회
-- 나간 기록에서 들어온 기록 빼면 될 것 같은데?
SELECT ANIMAL_ID, NAME
FROM (
    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_OUTS O
    MINUS
    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS I
)