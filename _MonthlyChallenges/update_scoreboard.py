import os
import json
from datetime import datetime

from update_dashboard import archive_current_month

SCOREBOARD_FILE = "scoreboard.json"
PR_DATA_FILE = "pr_data.json"

# 챌린지 설정 (매달 투표 결과로 정해진 유형과 목표 문제 수)
CHALLENGE_TYPES = {
    "그래프": 5,
    "DP": 5
}

def initialize_user():
    # 사용자별 초기 스코어보드 구조
    return {
        **{ctype: [] for ctype in CHALLENGE_TYPES.keys()},
        "achieved": {ctype: False for ctype in CHALLENGE_TYPES.keys()}
    }

def main():
    # 현재 달 문자열
    current_month = datetime.now().strftime("%Y-%m")

    # 1. 기존 스코어보드 로드 (없으면 빈 dict로 초기화)
    print("[Step 1] Loading scoreboard file...")
    if os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, 'r', encoding='utf-8') as f:
            try:
                scoreboard = json.load(f)
            except json.JSONDecodeError:
                scoreboard = {}
    else:
        scoreboard = {}

    print(f"[Step 1] Loaded scoreboard data: {scoreboard!r}")

    # 2-1. 새 구조("month", "users")가 없다면 변환
    print("[Step 2.1] Verifying scoreboard structure...")
    if "users" not in scoreboard or "month" not in scoreboard:
        scoreboard = {
            "month": current_month,
            "users": scoreboard  # 기존 scoreboard의 내용(사용자 데이터)이 있다면 여기에 넣음
        }
    else:
        # 2-2. month 값이 다르면 현재 달로 덮어쓰기
        print("[Step 2.2] Checking month field...")
        if scoreboard["month"] != current_month:
            print(f"[Step 2.2] Month mismatch detected (previous: {scoreboard['month']}, current: {current_month}); archiving...")

            archive_current_month()
            print("[Step 2.2] Archived previous month data to HISTORY.md")

            scoreboard["month"] = current_month
            scoreboard["users"] = {}  # 매달 유저값도 초기화
            print(f"[Step 2.2] Reset scoreboard for new month: {scoreboard!r}")

    users = scoreboard["users"]

    # 3. pr_data.json 파일 로드
    print("[Step 3] Loading PR data file...")
    if not os.path.exists(PR_DATA_FILE):
        print(f"[Step 3] PR data file not found: {PR_DATA_FILE}")
        exit(1)

    with open(PR_DATA_FILE, 'r', encoding='utf-8') as f:
        pr_data = json.load(f)

    print(f"[Step 3] Loaded PR data: {pr_data!r}")

    # 4. pr_data의 각 항목을 순회하며 사용자별 스코어보드 업데이트
    print("[Step 4] Processing PR data entries...")
    for entry in pr_data:
        username = entry["username"]
        algorithm = entry["algorithm"]
        problem_id = entry["problem_id"]

        if not username or not algorithm or problem_id is None:
            continue

        print(f"[Step 4] Entry details -> user: {username}, algorithm: {algorithm}, problem_id: {problem_id}")
        print(f"[Step 4] Current users state: {users!r}")
        # 챌린지 유형에 포함되어 있는지 확인 (예: "그래프", "DP")
        if algorithm not in CHALLENGE_TYPES:
            continue  # 챌린지 대상이 아니면 무시

        # 해당 사용자가 없으면 초기화
        if username not in users:
            print(f"[Step 4] Initializing user: {username}")
            users[username] = initialize_user()
            print(f"[Step 4] Users after initialization: {users!r}")

        # 해당 문제 ID 중복 없이 추가
        print(f"[Step 4] Adding problem ID {problem_id} for user '{username}'")
        if problem_id not in users[username].get(algorithm, []):
            users[username][algorithm].append(problem_id)

    # 5. 각 사용자별로 달성 여부 업데이트
    print("[Step 5] Updating achievement status for each user...")
    for username, data in users.items():
        for ctype, goal in CHALLENGE_TYPES.items():
            count = len(data.get(ctype, []))
            # 목표 수 이상이면 달성 처리
            data["achieved"][ctype] = (count >= goal)
    print(f"[Step 6] Achievement statuses: {users!r}")

    # 6. 스코어보드 저장
    print("[Step 6] Saving updated scoreboard to file...")
    with open(SCOREBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(scoreboard, f, ensure_ascii=False, indent=2)
        print(f"[Step 7] Successfully updated '{SCOREBOARD_FILE}'")

if __name__ == '__main__':
    main()
