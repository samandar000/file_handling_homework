def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i=0
    k=0
    for i in f:
        if i in ('0123456789'):
            k+=1
        answer = k , len(f)-k
    return list(answer)
f = open('txt_file/data05.txt').read()
print(main(f)) 
    
# Read data from file