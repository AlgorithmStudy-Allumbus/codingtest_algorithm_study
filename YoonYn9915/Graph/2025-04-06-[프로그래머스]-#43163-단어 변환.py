
# 두 단어가 한글자만 다른지 확인하는 함수
def count_same_letter(word1, word2):

    count = 0
    word_length = len(word1)
    # 모든 단어의 길이는 같으므로 단어의 길이만큼 반복문 돌면서 같은 글자 계산
    for i in range(word_length):
        if word1[i] == word2[i]:
            count += 1

    if word_length - 1 == count:
        return True
    else:
        return False



def dfs(begin, target, words, depth):
    global words_num
    global min_value

    # depth가 words의 크기보다 커지면 해당 탐색 종료
    if depth > words_num:
        return

    # begin과 target이 같다면 탐색 종료
    if begin == target:
        # 현재 depth와 최솟값 비교
        min_value = min(min_value, depth)
        return

    copy_words = words[:]

    for i in range(len(words)):
        # 두 단어가 한글자만 다르다면 그 단어로 변환
        if count_same_letter(begin, words[i]):
            # 단어 목록에서 현재 단어 제외하고
            removed_word = copy_words.pop(i)
            # 다음 detph dfs 실행
            dfs(removed_word, target, copy_words, depth + 1)
            # 배열 원복
            copy_words.insert(i, removed_word)




def solution(begin, target, words):

    # target이 words에 없어서 변환할 수 없는 경우
    if target not in words:
        return 0

    # 단어의 개수
    global words_num
    words_num = len(words)

    global min_value
    min_value = 10000

    dfs(begin, target, words, 0)

    return min_value