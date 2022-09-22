from gettext import find


def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    k=[]
    for i in f:
        if i.isdigit():
            k.append(int(i))
    return max(k)
f = open('txt_file/data08.txt').read()
f = f.split()
print(main(f))

# Read data from file