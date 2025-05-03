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
    """
    # 🔥{month} 챌린지 진행 상황

    ### 👉그래프
    - **{user}**: {count}개 {achieved_str}

    ### 👉DP
    - **{user}**: {count}개 {achieved_str}
    """
    month = scoreboard.get("month", "Unknown")
    users = scoreboard.get("users", {})

    # 월 챌린지 헤더 추가
    md = f"# 🔥{month} 챌린지 진행 상황\n\n"

    # 각 챌린지 유형별 섹션 생성
    for ctype in CHALLENGE_TYPES.keys():
        md += f"### 👉 {ctype}\n"
        for user, data in users.items():
            count = len(data.get(ctype, []))
            achieved = data.get("achieved", {}).get(ctype, False)
            achieved_str = "✅" if achieved else "❌"
            md += f"- **{user}**: {count}개 {achieved_str}\n"
        md += "\n\n"
    return md

def archive_current_month():
    """
    HISTORY_FILE에 현재 달 기록을 추가 (append 방식)
    """
    # 1. DASHBOARD.md 읽기
    try:
        with open(DASHBOARD_FILE, "r", encoding="utf-8") as db:
            dashboard_md = db.read()
    except FileNotFoundError:
        print("[Archive] DASHBOARD.md not found. Please create DASHBOARD.md first.")
        return

    # 2. HISTORY.md에 append
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(dashboard_md)
        f.write("\n\n")  # 구분용 빈 줄
    print("[Archive] Appended current dashboard to HISTORY.md successfully.")

def update_dashboard():
    # 1. scoreboard.json 로드
    print("[Step 1] Loading scoreboard file...")
    if not os.path.exists(SCOREBOARD_FILE):
        print(f"[Step 1] File not found: {SCOREBOARD_FILE}")
        return

    with open(SCOREBOARD_FILE, "r", encoding="utf-8") as f:
        scoreboard = json.load(f)
    print("[Step 1] Loaded scoreboard data.")

    # 2. 기존 파일 구조가 새 형식("month", "users")이 아니라면 변환
    print("[Step 2] Verifying scoreboard structure...")
    if "month" not in scoreboard or "users" not in scoreboard:
        # 기존 구조는 사용자 이름이 최상위 키인 형태
        scoreboard = {
            "month": datetime.now().strftime("%Y-%m"),
            "users": scoreboard
        }
        # 새 형식으로 저장
        with open(SCOREBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(scoreboard, f, ensure_ascii=False, indent=2)
        print("[Step 2] Converted existing scoreboard format to new structure.")

    # 3. DASHBOARD.md 파일 생성 및 업데이트
    print("[Step 3] Generating dashboard content...")
    md_content = generate_dashboard(scoreboard)
    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)

    print("[Step 3] DASHBOARD.md updated successfully.")

if __name__ == '__main__':
    update_dashboard()
