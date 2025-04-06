import os
import json
from datetime import datetime

SCOREBOARD_FILE = "scoreboard.json"
DASHBOARD_FILE = "DASHBOARD.md"
HISTORY_FILE = "HISTORY.md"

CHALLENGE_TYPES = {
    "그래프": 5,
    "DP": 5
}

def generate_dashboard(scoreboard):
    # scoreboard 구조 예시 (새로운 형식):
    # {
    #   "month": "2023-04",
    #   "users": {
    #       "user1": {
    #           "그래프": [101, 102],
    #           "DP": [2169, 1520],
    #           "achieved": {
    #               "그래프": true,
    #               "DP": false
    #           }
    #       },
    #       "user2": { ... }
    #   }
    # }
    month = scoreboard.get("month", "Unknown")
    users = scoreboard.get("users", {})

    md = f"# {month} 챌린지 진행 상황\n\n"
    md += "| 사용자 | 챌린지 유형 | 문제 수 | 달성 여부 |\n"
    md += "| ------ | ----------- | ------- | --------- |\n"

    # 각 사용자별 진행 상황 표 작성
    for user, data in users.items():
        for ctype in CHALLENGE_TYPES.keys():
            count = len(data.get(ctype, []))
            achieved = data.get("achieved", {}).get(ctype, False)
            achieved_str = "✅" if achieved else "❌"
            md += f"| {user} | {ctype} | {count} | {achieved_str} |\n"

    return md

def archive_current_month(scoreboard):
    # HISTORY_FILE에 현재 달 기록을 추가 (append 방식)
    dashboard_md = generate_dashboard(scoreboard)
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(dashboard_md)
        f.write("\n\n")  # 구분을 위한 빈 줄 추가
    print("HISTORY.md 업데이트 완료!")

def update_dashboard():
    # 1. scoreboard.json 로드
    if not os.path.exists(SCOREBOARD_FILE):
        print(f"{SCOREBOARD_FILE} 파일이 없습니다.")
        return

    with open(SCOREBOARD_FILE, "r", encoding="utf-8") as f:
        scoreboard = json.load(f)

    # 2. 기존 파일 구조가 새 형식("month", "users")이 아니라면 변환
    if "month" not in scoreboard or "users" not in scoreboard:
        # 기존 구조는 사용자 이름이 최상위 키인 형태
        scoreboard = {
            "month": datetime.now().strftime("%Y-%m"),
            "users": scoreboard
        }
        # 새 형식으로 저장
        with open(SCOREBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(scoreboard, f, ensure_ascii=False, indent=2)
        print("기존 scoreboard 형식을 새 구조로 변환하였습니다.")

    # 3. 현재 달 확인 및 월 초기화 처리
    current_month = datetime.now().strftime("%Y-%m")
    stored_month = scoreboard.get("month", current_month)
    print(f"현재 달: {current_month}, 저장된 달: {stored_month}")

    if stored_month != current_month:
        print(f"새로운 달({current_month})로 넘어감 - 이전 달({stored_month}) 기록을 히스토리에 저장합니다.")
        archive_current_month(scoreboard)
        # scoreboard 초기화: users는 빈 dict, month는 현재 달로 갱신
        scoreboard = {
            "month": current_month,
            "users": {}
        }
        with open(SCOREBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(scoreboard, f, ensure_ascii=False, indent=2)

    # 4. DASHBOARD.md 파일 생성 및 업데이트
    md_content = generate_dashboard(scoreboard)
    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)

    print("DASHBOARD.md 업데이트 완료!")

if __name__ == '__main__':
    update_dashboard()
