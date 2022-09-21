def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    k = 0
    i = 0
    for i in f:
        if i in ('0123456789'):
            k+=1
        
    return k
f = open('txt_file/data07.txt').read()

print(main(f))
    
# Read data from file