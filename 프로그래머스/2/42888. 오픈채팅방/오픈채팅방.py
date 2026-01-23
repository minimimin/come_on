def solution(record):
    answer = []
    # 중복 닉네임 허용, 유저 아이디로 구분 가능
    # O(N)
    user = {}
    for com in record:
        command = com.split()
        if command[0] in ["Enter", "Change"]:
            user[command[1]] = command[2]

    for logs in record:
        log = logs.split()
        if log[0] == "Enter":
            answer.append(user[log[1]]+"님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(user[log[1]]+"님이 나갔습니다.")
    return answer