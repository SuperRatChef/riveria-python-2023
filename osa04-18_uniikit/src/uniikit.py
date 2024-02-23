# tee ratkaisu tänne
def uniikit(lista):
    return sorted(list(set(lista)))

if __name__ == "__main__":
    print(uniikit([3, 2, 2, 1, 3, 3, 1]))