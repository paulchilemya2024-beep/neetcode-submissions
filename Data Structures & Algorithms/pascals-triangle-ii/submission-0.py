class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [1]

        for i in range(rowIndex):
            temp = [0] * (len(res)+1)
            for j in range(len(res)):
                temp[j] += res[j]
                temp[j+1] += res[j]
            res = temp
        return res