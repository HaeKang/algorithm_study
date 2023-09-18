# https://www.acmicpc.net/problem/1283
import sys
input = sys.stdin.readline

n = int(input())
word_dict = {}
result_word = []

for _ in range(n):
    words = input().rstrip()
    words = words.split(" ")
    flag = False

    for idx, word in enumerate(words):
        if word[0].upper() not in word_dict:
            word_dict[word[0].upper()] = 1
            flag = True
            words[idx] = "[" + word[0] + "]" + word[1:]
            print(' '.join(words))
            break

    flag2 = False
    if flag == False:
        for idx, word in enumerate(words):
            for i in range(len(word)):
                if word[i].upper() not in word_dict:
                    word_dict[word[i].upper()] = 1
                    flag2 = True
                    words[idx] = word[:i] + "[" + word[i] + "]" + word[i+1:]
                    print(' '.join(words))
                    break

            if flag2:
                break

    if flag == False and flag2 == False:
        print(' '.join(words))
