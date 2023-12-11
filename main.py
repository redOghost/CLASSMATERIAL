import csv
import heapq
from collections import defaultdict
from readData import read_data
from sort import sort_animals_by_priority, sort_locations_by_avg_weights, sort_animals_in_location_by_priority

# 동물 정보 읽어오기
animals_info = read_data('data.csv')


while True:
    print("동물 복지 현황 보기")
    print("1. 동물원의 모든 동물을 정렬하기")
    print("2. 동물사 선택하기")
    print("3. 동물사를 정렬하기")
    print("4. 종료")

    num = input("번호: ")

    # 전체 동물 가중치를 기준으로 정렬해서 출력
    if num == '1':
        sorted_ani = sort_animals_by_priority(animals_info)
        for animal in sorted_ani:
            print(f"{animal[1]} - 가중치: {-animal[0]}")
        print()

    # 선택한 동물사에 속한 동물 가중치를 기준으로 정렬해서 출력
    elif num == '2':
        print("동물사 목록")
        location_name = set()
        for animal in animals_info:
            location_name.add(animal['동물사'])
        print(location_name)
        print()
        selected_location = input("선택한 동물사의 이름을 입력하세요: ")
        sorted_animals_in_location = sort_animals_in_location_by_priority(animals_info, selected_location)
        for animal in sorted_animals_in_location:
            print(f"{animal[1]} - 가중치: {-animal[0]}")
        print()

    # 각 동물사의 가중치 평균을 기준으로 정렬해서 출력
    elif num == '3':
        sorted_locations = sort_locations_by_avg_weights(animals_info)
        for location in sorted_locations:
            print(f"{location[1]} - 가중치 평균: {-location[0]} ")
        print()

    elif num == '4':
        print("종료합니다.")
        break

    else:
        print("다시 선택하세요.")
