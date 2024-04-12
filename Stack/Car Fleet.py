class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        pos_speed.sort()
        pos_speed.reverse()
        fleet = []
        for pos, speed in pos_speed:
            if not fleet:
                fleet.append([pos, speed])
            else:
                prev_pos, prev_speed = fleet[-1][0], fleet[-1][1]
                is_meet = self.is_meet(target, prev_pos, prev_speed, pos, speed)
                if not is_meet:
                    fleet.append([pos, speed])
                

        return len(fleet)

    def is_meet(self, target, former_pos, former_speed, latter_pos, latter_speed):
        former_time = (target - former_pos) / former_speed
        latter_time = (target - latter_pos) / latter_speed
        return latter_time <= former_time


