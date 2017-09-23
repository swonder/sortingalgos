import random

def createRandomList(size = 0):
    num_list = []
    for i in range(size):
        rand_num = random.randint(0, size-1)
        num_list.append(rand_num)
    return num_list

#Average and worst case O(n^2)
#Can do in less lines of code!!
def insertionSort(lst = []):
    if len(lst) == 0:
        return []
    srt = []
    srt.append(lst.pop()) #Take the last element and put it into the sorted list
    while len(lst) > 0:
        last = lst.pop() #Pop the last element off the unsorted list
        for i in range(0, len(srt)):
            if len(srt) == 1: #This is the first and only element
                srt.append(last) if last > srt[i] else srt.insert(0, last)
            else: #More than one element
                if i < len(srt)-1:
                    if i == 0 and last <= srt[i]:
                        srt.insert(0, last)
                    elif last > srt[i] and last <= srt[i+1]:
                        srt.insert(i+1, last)
                else:
                    srt.append(last)
    return srt
    
def main():
    random.seed()
    for i in range(0, 50):
        s = random.randint(1,15)
        rl = createRandomList(s)
        print("Unsorted", rl)
        print("Sorted", insertionSort(rl))

    #l = [2, 0, 5, 2, 4, 2, 8, 7, 0]
    #print("Unsorted", l)
    #print("Sorted", insertionSort(l))

if __name__ == "__main__":
    main()
