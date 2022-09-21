def main(data):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    k = []
    i = 0
    while i < len(data) :
        if data[i] not in '0123456789':
            k.append(data[i])
        i+=1
    return k
f = open('txt_file/data03.txt').read()
print(main(f))
# Read data from file