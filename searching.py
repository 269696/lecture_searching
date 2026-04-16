import json
from generators import unordered_sequence
import time
import matplotlib.pyplot as plt



def read_data(file_name, field):

    if field not in{"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        None
    else:
        print(field)

    with open(file_name, "r") as file_obj:
        data=json.load(file_obj)
        s=data[field]
        return s





def linear_search(sekvence, cislo):
    pozice=[]
    count=0
    for index, hodnota in enumerate(sekvence):
        if hodnota == cislo:
            pozice.append(index)
            count += 1

    return {"positions":pozice,
            "count": count}

def binary_search(seznam, cislo):
    prava =len(seznam) - 1
    leva = 0


    while prava > leva:
        stred = (leva + prava) // 2
        if seznam[stred] < cislo:
            leva = leva + 1
        elif seznam[stred] > cislo:
            prava = prava -1
        else:
            return stred


times = []
rada = unordered_sequence(1000)
start = time.perf_counter()
linear_search(rada, 9)
end = time.perf_counter()
duration = end - start
print(f"Doba výpočtu lineární: {duration:.8f} ")
times = times.append(duration)
print(times)



def main():
    sequential_data=read_data("sequential.json","ordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data,9))
    print(binary_search(sequential_data, 23))



if __name__ == '__main__':
    main()