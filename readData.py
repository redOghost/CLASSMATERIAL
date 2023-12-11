from collections import defaultdict
import csv

# CSV 파일에서 동물 정보 읽어오기
def read_data(filepath):
    animals = [] #읽어온 모든 동물
    with open(filepath, newline='') as file:
        read = csv.DictReader(file)
        for row in read: #행별로 동물 읽기
            animal = {
                '이름':row['name'],
                '동물사':row['area'],
                '개체 수':int(row['weight1']),
                '서식 환경':int(row['weight2']),
                '노출':int(row['weight3'])
            }
            animals.append(animal)
    return animals