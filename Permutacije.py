def permutations(array):
    if len(array) == 1:
        return [array]

    all_permutations = []
    for i in range(len(array)):
        current = array[i]
        leftover = array[:i] + array[i+1:]
        for p in permutations(leftover):
            all_permutations.append([current] + p)

    return all_permutations

def getInput():
    q = input("Input an array of integers, separated by spaces: ")
    brojevi = list(map(int, q.split()))
    return brojevi

def printPermutations(p):
    for per in p:
        print(" ".join(map(str, per)))
    

def startPermutations():
    try: 
        s = getInput()
        printPermutations(permutations(s))
    except:
        print("Invalid array!")
        
startPermutations()