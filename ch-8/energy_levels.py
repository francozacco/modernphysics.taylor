from rich import print

def E_fn(n_x, n_y):
    return ((n_x**2)/(1.1**2)) + (n_y**2)

def main():

    E = {}
    for n_x in range(1, 10):
        for n_y in range(1, 10):
            E[(n_x, n_y)] = E_fn(n_x, n_y)
    
    sorted_items = sorted(E.items(), key=lambda x: x[1])
    print(sorted_items)


if __name__ == "__main__":
    main()