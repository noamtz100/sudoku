
from typing import List


class Tile:
    def __init__(self, num, y, x):
        self.value = num
        self.group = (y//3)*3+x//3
        self.avaible = self.value == '0'
        if self.avaible:
            self.whitelist = "123456789"
        else:
            self.whitelist = ""
        self.y = y
        self.x = x

    def __repr__(self) -> str:
        return f"{self.value}"


class Table:
    def __init__(self, filename):
        self.lst: List[Tile] = list()
        with open(filename, "r") as file1:
            for i, line in enumerate(file1.readlines()):
                # self.lst.append(list())
                for j in range(9):
                    # self.lst[-1].append(Tile(line[j], i, j))
                    self.lst.append(Tile(line[j], i, j))

    def check_tile(self, t: Tile) -> str:
        if t.avaible:
            for item in self.lst:
                if (not item.avaible) and (item.x == t.x or item.y == t.y or item.group == t.group) and item.value in t.whitelist:
                    t.whitelist = t.whitelist.replace(item.value, "")
            if len(t.whitelist) == 1:
                t.avaible = False
                t.value = t.whitelist
            if len(t.whitelist) == 0:
                print(self)
                raise Exception(f"Bug tile ({t.y + 1}, {t.x + 1})")

    def check_if_all_finished(self):
        flag = False
        for item in self.lst:
            if item.avaible:
                self.check_tile(item)
                flag = True
        return flag
    
    def __repr__(self) -> str:
        s=''
        for i,ch in enumerate(self.lst):
            if i%9 == 0:
                s+="\n"
            s+=f"{ch} "
        return s[1:]


t = Table("table.txt")
print(t)
f = True
print("------------------")
while (f):
    f = t.check_if_all_finished()
print(t)
