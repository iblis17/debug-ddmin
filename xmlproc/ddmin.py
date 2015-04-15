from split import split
from tests import test_xmlproc, ExecError


MAX_DEGREE = 10

def ddmin(test_func, filename, n=1):
    with open(filename) as f:
        data = f.read()
        last_failed_file = None

        for i in xrange(n, MAX_DEGREE):
            for d in split(data, i):
                try:
                    test_xmlproc(d)
                except ExecError as e:
                    last_failed_file = e.filename
                    return ddmin(test_xmlproc, e.filename, 2)
                except:
                    pass
        if last_failed_file is None:
            return filename
        return last_failed_file


if __name__ == '__main__':
    f = ddmin(test_xmlproc, './demo/urls.xml')
    print('=====================================')
    print('found the failed input @ {}'.format(f))
    print('=====================================')
