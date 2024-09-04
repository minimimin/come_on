# DFS 활용해서 전체 단어 문맥 만들기
def solution(word):
    all_word = set()
    gather = ['A', 'E', 'I', 'O', 'U']
    def dfs(cnt, letter):
        if cnt > 5:
            return
        all_word.add(letter)
        for i in range(5):
            dfs(cnt+1, letter + gather[i])
    dfs(0,"")
    final_dic = sorted(list(all_word))
    return final_dic.index(word)