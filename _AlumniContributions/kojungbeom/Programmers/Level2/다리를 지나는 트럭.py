def solution(bridge_length, weight, truck_weights):
    bridge = []
    all_weight = 0
    t = 0
    while truck_weights or bridge:
        t += 1

        if bridge and t - bridge[0][1] == bridge_length:
            truck, _ = bridge.pop(0)
            all_weight -= truck

        if truck_weights and all_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append([truck, t])
            all_weight += truck

    return t