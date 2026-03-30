class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = 1
        max_cnt = 1
        for i in range(0, len(fruits)):
            l = [fruits[i]]
            type_cnt = 1
            cnt = 1
            for j in range(i+1, len(fruits)):
                if fruits[j] not in l:
                    if type_cnt < 2:
                        type_cnt += 1
                        cnt += 1
                        l.append(fruits[j])
                        if max_cnt < cnt:
                            max_cnt = cnt
                    else:
                        break
                else:
                    cnt += 1
                    if max_cnt < cnt:
                        max_cnt = cnt
        return max_cnt

                
