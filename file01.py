def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open ('data01.txt', 'r')
    data = f.read()
    return str(data)


