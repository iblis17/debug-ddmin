from tempfile import NamedTemporaryFile
from xml.parsers.xmlproc import xmlproc


TMP_DIR = './tmp'


class ExecError(Exception):
    def __init__(self, filename):
        self.filename = filename


def test_xmlproc(data):
    p = xmlproc.XMLProcessor()
    f = get_tempfile(data)
    try:
        p.parse_resource(f)
    except Exception as e:
        print('Error file: {}'.format(f))
        raise ExecError(f)
    else:
        import os
        os.remove(f)


def get_tempfile(s):
    '''
    :param s: the str that writed into tempfile.
    '''
    f = NamedTemporaryFile(dir=TMP_DIR, delete=False)
    f.file.write(s)
    f.file.flush()
    f.close()
    return f.name
