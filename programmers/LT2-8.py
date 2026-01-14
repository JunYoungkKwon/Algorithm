# [벡준] 이모티콘
from collections import deque


def solution():
    S = int(input())

    # visited[화면 이모티콘 수][클립보드 이모티콘 수]
    visited = [[-1] * (S + 1) for _ in range(S + 1)]

    q = deque()
    q.append((1, 0))  # (화면, 클립보드)
    visited[1][0] = 0

    while q:
        screen, clip = q.popleft()

        # 목표 도달
        if screen == S:
            print(visited[screen][clip])
            return

        # 1️⃣ 복사 (화면 → 클립보드)
        if visited[screen][screen] == -1:
            visited[screen][screen] = visited[screen][clip] + 1
            q.append((screen, screen))

        # 2️⃣ 붙여넣기 (클립보드 → 화면)
        if clip > 0 and screen + clip <= S:
            if visited[screen + clip][clip] == -1:
                visited[screen + clip][clip] = visited[screen][clip] + 1
                q.append((screen + clip, clip))

        # 3️⃣ 삭제 (화면 - 1)
        if screen > 0:
            if visited[screen - 1][clip] == -1:
                visited[screen - 1][clip] = visited[screen][clip] + 1
                q.append((screen - 1, clip))


solution()
