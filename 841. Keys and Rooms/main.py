class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # method 1:
        # 用一个stack来记录接下来要去的房间
        # 当进入一个新的房间，房间见过状态更新，把接下来要去的放进stack
        seen = [False] * len(rooms)
        seen[0] = True
        todo_list = [0]
        while todo_list:
            next_room = todo_list.pop()
            for nr in rooms[next_room]:
                if seen[nr] is False:
                    seen[nr] = True
                    todo_list.append(nr)
        return all(seen)
