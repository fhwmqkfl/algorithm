### https://leetcode.com/problems/group-anagrams/
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# 1. 처음 접근방법 
# 결과를 리턴할 리스트를 만들고 for 문을 돌며 sorted() 함수를 이용해 결과 리턴 리스트에 해당 배열이있는지 확인후 추가하는 방법을 생각했다 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        for i in strs:
            word = sorted(i)
            # 빈리스트는 일단 값 무조건 추가
            if len(result) == 0:
                result.append([i])
            else:
                # a리스트에 값이 있으니 하나씩 꺼내보기
                cnt = 0
                for j in result:
                    c_word = sorted(j[0])
                    # 같은 값이면 비교군쪽에 단어 추가해주기
                    if word == c_word:
                        j.insert(0,i)
                        cnt = 1
                if cnt == 0:
                    result.append([i])
        return result

# 실행 결과 : Time Limit Exceeded
# 117개의 테스트케이스증 111번째에서 초과되었다.

# 접근방법. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}

        for string in strs:
            # "eat"라는 단어를 재정렬
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())
