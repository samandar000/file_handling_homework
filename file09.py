def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: re0sturn answer
    """
    k = []
    l = 0 
    for i in f:
        if i in '0123456789':
            k.append(int(i))
    
    return l

f = open('txt_file/data09.txt').read().split()
print(main(f))
# Read data from file