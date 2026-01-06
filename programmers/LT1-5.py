def is_match(user, banned):
    if len(user) != len(banned):
        return False

    for u, b in zip(user, banned):
        if b == '*':
            continue
        if u != b:
            return False
    return True


def solution(user_id, banned_id):
    result = set()
    n = len(banned_id)

    # 1️⃣ banned_id별 가능한 user 목록
    candidates = []
    for ban in banned_id:
        temp = []
        for user in user_id:
            if is_match(user, ban):
                temp.append(user)
        candidates.append(temp)

    # 2️⃣ DFS
    def dfs(idx, used):
        if idx == n:
            result.add(frozenset(used))
            return

        for user in candidates[idx]:
            if user not in used:
                dfs(idx + 1, used + [user])

    dfs(0, [])
    return len(result)
