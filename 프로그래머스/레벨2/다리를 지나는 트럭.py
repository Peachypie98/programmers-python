from collections import deque
def solution(bridge_length, weight, truck_weights):
    value = 0
    sum1 = 0
    truck_count = 0
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    while(len(truck_weights) != 0):
        for i in truck_weights:
            value += i
            if(value <= weight and truck_count != bridge_length):
                a = bridge.popleft()
                if (a != 0):
                    truck_count -=1
                    sum1 -= a
                bridge.append(i)
                time += 1
                truck_count += 1
                truck_weights.remove(i)
                sum1 += i
                break
            else:
                x = bridge.popleft()
                time += 1
                if(x != 0):
                    truck_count -= 1
                    sum1 -= x
                value = sum1 + truck_weights[0]
                if(value <= weight and len(truck_weights) != 0):
                    a = truck_weights.popleft()
                    bridge.append(a)
                    truck_count += 1
                    sum1 += a
                    value = sum1
                else:
                    value = sum1
                    bridge.append(0)
                break
            
    while(truck_count != 0):
        x = bridge.popleft()
        time += 1
        if(x != 0):
            truck_count -= 1
        bridge.append(0)
    return time