

def open_Document(filename):
    try:
        with open(filename, 'r') as fp:
            text = fp.read()
        return text
    except:
        return "ERROR"