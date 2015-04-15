

def split(data, n):
    '''
    :type data: str
    :param data: input data
    :param split: slice number
    :return: a list of subsets
    '''
    if not data:
        return []

    data = data.splitlines()
    glue = '\n'
    if len(data) == 1:
        data = data[0]
        glue = ''

    step = int(len(data) / n)

    if step == 0:
        return []

    return chunks(data, step, glue)

def chunks(l, n, glue):
    for i in xrange(0, len(l), n):
        yield glue.join(l[i:i+n])
