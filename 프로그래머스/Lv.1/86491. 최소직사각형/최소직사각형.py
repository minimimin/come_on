def solution(sizes):
    w = []
    h = []
    for i, j in sizes:
        if i >= j:
            w.append(i)
            h.append(j)
            continue
        h.append(i)
        w.append(j)
    return max(w) * max(h)