def solution(n, lost, reserve):
    all_students = [1 for _ in range(n)]
    for i in lost:
        all_students[i-1] = 0
    for j in reserve:
        all_students[j-1] += 1
    
    if all_students[0] == 0 and all_students[1] > 1:
        all_students[0] += 1
        all_students[1] -= 1
        
    for student_num in range(1,n-1):
        if not all_students[student_num]:
            if all_students[student_num-1] > 1:
                all_students[student_num-1] -= 1
                all_students[student_num] += 1
            elif all_students[student_num+1] > 1:
                all_students[student_num+1] -= 1
                all_students[student_num] += 1

    if not all_students[n-1] and all_students[n-2] > 1:
        all_students[n-1] += 1
        all_students[n-2] -= 1
    
    answer = len(list(filter(lambda std:std>0, all_students)))
    return answer