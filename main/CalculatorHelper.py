
def getNumbers(num_string, s):
    result = []
    for string in num_string.split(s):
        result.append(int(string))
    is_there_negatives(result)
    return filter(lambda x: x < 1000, result)


def is_there_negatives(result):
       negative = filter(lambda x: x < 0, result)
       if len(negative) != 0:
           raise Exception(negative)
