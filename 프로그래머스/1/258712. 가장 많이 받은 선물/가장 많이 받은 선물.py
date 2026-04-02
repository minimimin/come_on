def solution(friends, gifts):
    frd_dict = {friend:[0,{friend:0 for friend in friends}] for friend in friends}
    next_mon_dict = {friend:0 for friend in friends}
    
    for gift in gifts:
        give, take = gift.split(" ")
        frd_dict[give][0] += 1
        frd_dict[take][0] -= 1
        frd_dict[give][1][take] += 1
    
    for me in friends:
        for friend in friends:
            if me == friend:
                continue
            elif frd_dict[me][1][friend] > frd_dict[friend][1][me]:
                next_mon_dict[me] += 1
                continue
            elif frd_dict[me][1][friend] == frd_dict[friend][1][me] and frd_dict[me][0] > frd_dict[friend][0]:
                next_mon_dict[me] += 1
                continue
                
    return max(next_mon_dict.values())