import heapq
from collections import defaultdict

# 전체 동물 복지 순 정렬
def sort_animals_by_priority(animals):
    allWeight= [(-(animal['개체 수']+animal['서식 환경']+animal['노출']), animal['이름']) for animal in animals]  # 복지를 우선순위로 하는 최대 힙
    heapq.heapify(allWeight)
    sorted_animals = []
    while allWeight:
        animal = heapq.heappop(allWeight)
        sorted_animals.append(animal)
    return sorted_animals

# 선택한 관에 속한 동물 복지 순 정렬
def sort_animals_in_location_by_priority(animals, selected_location):
    animals_in_location = [animal for animal in animals if animal['동물사'] == selected_location]
    return sort_animals_by_priority(animals_in_location)

# 동물사 정렬
def sort_locations_by_avg_weights(animals):
    location_weights = defaultdict(list)
    for animal in animals:
        location_weights[animal['동물사']].append(animal['개체 수']+animal['서식 환경']+animal['노출'])

    avg_weights = {location: sum(weights) / len(weights) for location, weights in location_weights.items()}
    heap = [(-weight, location) for location, weight in avg_weights.items()]  # 가중치를 우선순위로 하는 최소 힙
    heapq.heapify(heap)
    sorted_locations = []
    while heap:
        location = heapq.heappop(heap)
        sorted_locations.append(location)
    return sorted_locations