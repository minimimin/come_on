def solution(name):
    joy_stick = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}

    answer = len(name)-1
    visited = [1 if c=='A' else 0 for c in name]
    n = len(name)

    def find_path(temp_answer, visited, start):
        nonlocal answer

        # 모두 방문했으면(=수평 이동 끝났으면) answer 후보 갱신
        if all(visited):
            if temp_answer < answer:
                answer = temp_answer
            return

        # 현재 위치 처리
        if name[start] != 'A' and not visited[start]:
            visited[start] = 1
            # 여기서는 수평 이동을 추가하지 않음(수직은 마지막에 더함)
            # 다음으로 갈 두 방향 후보를 "점프" 방식으로 생성해서 내려감

            # pruning
            if temp_answer >= answer:
                visited[start] = 0
                return

            # 오른쪽으로 다음 목표까지 거리/인덱스 찾기
            right_dist = 0
            right_idx = start
            while True:
                right_idx = (right_idx + 1) % n
                right_dist += 1
                if not visited[right_idx] and name[right_idx] != 'A':
                    break
                # 모두 방문 직전이면 루프가 끝나지 않을 수도 있으니 보호
                if right_dist >= n:
                    break

            # 왼쪽으로 다음 목표까지 거리/인덱스 찾기
            left_dist = 0
            left_idx = start
            while True:
                left_idx = (left_idx - 1 + n) % n
                left_dist += 1
                if not visited[left_idx] and name[left_idx] != 'A':
                    break
                if left_dist >= n:
                    break

            # 다음 목표가 없으면(모두 방문 상태에 가까움) 종료 처리
            # all(visited)에서 걸리는 게 보통이지만, 방어적으로 한 번 더
            if right_dist >= n and left_dist >= n:
                if temp_answer < answer:
                    answer = temp_answer
                visited[start] = 0
                return

            # 두 방향 재귀 분기 (수평이동 거리만 더함)
            if right_dist < n:
                find_path(temp_answer + right_dist, visited, right_idx)
            if left_dist < n:
                find_path(temp_answer + left_dist, visited, left_idx)

            visited[start] = 0

        else:
            # 현재 칸이 A거나 이미 방문했다면, '한 칸씩'이 아니라
            # 다음 목표까지 점프해서 이동 분기
            if temp_answer >= answer:
                return

            # 오른쪽 점프
            right_dist = 0
            right_idx = start
            found_right = False
            while right_dist < n:
                right_idx = (right_idx + 1) % n
                right_dist += 1
                if not visited[right_idx] and name[right_idx] != 'A':
                    found_right = True
                    break

            # 왼쪽 점프
            left_dist = 0
            left_idx = start
            found_left = False
            while left_dist < n:
                left_idx = (left_idx - 1 + n) % n
                left_dist += 1
                if not visited[left_idx] and name[left_idx] != 'A':
                    found_left = True
                    break

            if not found_right and not found_left:
                # 더 갈 곳이 없으면 종료
                if temp_answer < answer:
                    answer = temp_answer
                return

            if found_right:
                find_path(temp_answer + right_dist, visited, right_idx)
            if found_left:
                find_path(temp_answer + left_dist, visited, left_idx)

    # 시작: 0번에서 탐색
    find_path(0, visited, 0)

    # 마지막에 수직 조작(알파벳 위/아래) 비용 더하기
    for char in name:
        answer += joy_stick[char]
    return answer
