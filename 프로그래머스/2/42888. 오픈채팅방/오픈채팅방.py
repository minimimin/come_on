from collections import defaultdict

def solution(record):
    answer = []
    # 중복 닉네임 허용, 유저 아이디로 구분 가능
    # O(N)
    user = defaultdict(str)
    logs = []
    for com in record:
        command = com.split()
        if command[0] == "Enter":
            user[command[1]] = command[2]
            logs.append(("Enter", command[1]))
        elif command[0] == "Leave":
            logs.append(("Leave", command[1]))
        else:
            user[command[1]] = command[2]
    for log in logs:
        if log[0] == "Enter":
            answer.append(user[log[1]]+"님이 들어왔습니다.")
        else:
            answer.append(user[log[1]]+"님이 나갔습니다.")
    return answer