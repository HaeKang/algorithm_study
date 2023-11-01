# https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/?envType=study-plan-v2&envId=top-interview-150

class WordDictionary:

    def __init__(self):
        self.root = {}
        self.flag = False
        

    def addWord(self, word: str) -> None:
        cur_dict = self.root
        for c in word:
            if c not in cur_dict:
                cur_dict[c] = {}
            cur_dict = cur_dict[c]
        cur_dict[self.flag] = True
        

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, idx, cur_dict):
        if idx == len(word):
            if self.flag in cur_dict:
                return True
            else:
                return False
        
        if word[idx] == '.':
            for next_word in cur_dict:
                if next_word != self.flag:
                    found = self.dfs(word, idx + 1, cur_dict[next_word])
                    if found:
                        return True
        else:
            if word[idx] in cur_dict:
                return self.dfs(word, idx + 1, cur_dict[word[idx]])
            
        return False
