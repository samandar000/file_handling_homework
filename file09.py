def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: re0sturn answer
    """
    k = []
    for i in f:
        if i.isdigit():
            k.append(int(i))
    return min(k)
f = open('txt_file/data09.txt').read().split()
print(main(f))
# Read data from file