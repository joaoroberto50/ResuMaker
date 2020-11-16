from textract import process


def open_doc(filename):
    try:
        text = process(filename)
        return text.decode("utf-8")
    except:
        return 'ERROR'