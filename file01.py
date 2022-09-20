def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = data.split(',')
    i = 0
    while i < len(data):
        
        data[i] = int(data[i])
        i+=1
    return data
f = open('txt_file/data01.txt').read()

print(main((f)))