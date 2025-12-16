def solution(sizes):
    max_w = 0
    max_h = 0
    for y, x in sizes:
        h, w = max(y, x), min(y, x)
        max_h = max(max_h, h)
        max_w = max(max_w, w)

    return max_w * max_h