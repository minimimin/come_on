def solution(sizes):
    w = set()
    h = set()
    for i, j in sizes:
        if i >= j:
            w.add(i)
            h.add(j)
            continue
        h.add(i)
        w.add(j)
    return max(list(w)) * max(list(h))