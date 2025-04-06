import os
import json
import re


def main():
    # 1. GitHub 이벤트 페이로드 로드
    event_path = os.getenv('GITHUB_EVENT_PATH')
    print("event_path", event_path)
    if not event_path:
        print("GITHUB_EVENT_PATH 환경변수가 설정되어 있지 않습니다.")
        exit(1)

    with open(event_path, 'r', encoding='utf-8') as f:
        event_data = json.load(f)
        print(f"event_data: {event_data}")

    pr_body = event_data['pull_request']['body']
    pr_number = event_data['pull_request']['number']
    username = event_data['pull_request']['user']['login']
    print(f"pr_body: {pr_body}, pr_number: {pr_number}")

    if pr_number is None:
        print("PR 번호를 찾을 수 없습니다.")
        exit(1)

    # 2. PR 본문을 줄 단위로 분할
    lines = pr_body.splitlines()
    print(f"lines: {lines}")

    # 3. "푼 문제" 섹션 탐지 및 문제 항목 파싱
    in_problem_section = False
    problem_entries = []

    # 정규표현식 패턴:
    # - [백준 #2169. 로봇 조종하기](https://www.acmicpc.net/problem/2169): DP / 골드2
    pattern = r'- \[(?P<source>[^\]]+?) #(?P<id>\d+)\.\s+(?P<title>.*?)\]\((?P<link>.*?)\):\s*(?P<algorithm>[^/]+)\s*/\s*(?P<difficulty>.+)'

    for line in lines:
        # "푼 문제" 키워드를 찾으면 해당 섹션 시작으로 설정
        if "푼 문제" in line:
            in_problem_section = True
            continue

        if in_problem_section:
            # bullet list 항목만 처리
            if line.startswith('- '):
                match = re.match(pattern, line)
                print(f"match: {match}")
                if match:
                    entry = match.groupdict()
                    print(f"entry: {entry}")
                    # 문제 번호를 정수로 변환
                    entry['problem_id'] = int(entry.pop("id"))
                    entry['pr_number'] = pr_number
                    entry['username'] = username
                    # 공백 제거
                    entry['algorithm'] = entry['algorithm'].strip()
                    entry['difficulty'] = entry['difficulty'].strip()
                    problem_entries.append(entry)
                    print(f"problem_entries: {problem_entries}")

    # 4. 추출된 데이터를 pr_data.json 파일에 저장
    with open("pr_data.json","w", encoding='utf-8') as f:
        json.dump(problem_entries, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
