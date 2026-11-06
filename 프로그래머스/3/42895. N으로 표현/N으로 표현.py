def solution(N, number):
    
    if N == number:
        return 1
    
    # 사용되는 숫자에 따라 만들 수 있는 모든 값 set(중복 방지용)에 넣어두기
    # n개의 set이 있는 리스트 만들기(단, 인덱스+1이 번호임)
    make_set = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    # 1개 사용, 2개 사용, 3개 사용(=1개 사용과 2개 사용 조합), 앞으로 그 이후 조합들은 그만큼의 것들 더해서 계산
    
    # 2개 사용했을 때 나올 수 있는 연산값들 구하기
    if N+N == number or N-N == number or N*N == number or N//N == number or int(str(N)*2) == number:
        return 2
    else:
        make_set[1].update([N+N,N-N,N*N,N//N])
    
    # 각 갯수별 나올 수 있는 조합 구하기
    for idx in range(3, 9):
        if number in make_set[idx-1]:
            return idx
        for case in range(1, idx):
            for fir in make_set[case-1]:
                for sec in make_set[idx-case-1]:
                    if fir+sec == number or fir-sec == number or fir*sec == number:
                        return idx
                    elif not sec:
                        make_set[idx-1].update([fir+sec,fir-sec,fir*sec,0])
                    else:
                        if not fir%sec:
                            if fir//sec == number:
                                return idx
                            make_set[idx-1].update([fir+sec,fir-sec,fir*sec,fir//sec])
                        else:
                            make_set[idx-1].update([fir+sec,fir-sec,fir*sec])

    return -1