from dataclasses import dataclass


@dataclass
class Solution:
    s: str
    numRows: int

    def convert(self) -> str:

        if self.numRows == 1:
            return self.s

        zigzag_arr = [[0 for _ in range(len(self.s))] for _ in range(self.numRows)]

        i, j = 0, 0
        switch = False  # False means traversing downwards
        counter = 0
        for idx in range(len(self.s)):
            if not switch:
                zigzag_arr[i][j] = self.s[idx]
                i += 1
                counter += 1
            else:
                zigzag_arr[i][j] = self.s[idx]
                i -= 1
                j += 1
                counter -= 1

            if (counter == self.numRows) and (switch == False):
                switch = True  # Traversing upwards
                i -= 2
                j += 1
            elif (counter == 1) and (switch == True):
                switch = False
                i += 2
                j -= 1

        result_str = ""
        for i in zigzag_arr:
            for j in i:
                if j != 0:
                    result_str += j

        return result_str


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution(s, numRows)
    print(solution.convert())



