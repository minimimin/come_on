min_cnt = 1000000

def DFS(begin, target, words, is_here, count):
    global min_cnt
    if begin == target:
        if min_cnt > count:
            min_cnt = count
        return
    else:
        for word in words:
            if word not in is_here:
                temp_cnt = 0
                for i in range(len(begin)):
                    if begin[i] != word[i]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    is_here.add(word)
                    DFS(word, target, words, is_here, count+1)
                    is_here.remove(word)

def solution(begin, target, words):
    global min_cnt
    if target not in words:
        return 0
    is_here = set()
    DFS(begin, target, words, is_here, 0)
    return min_cnt