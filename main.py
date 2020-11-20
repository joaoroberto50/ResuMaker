from src.resumer import resumer
from src.getpage import get_page
from src.openpdf import open_doc
from src.opentxt import open_Text
from sys import argv


def help():
    return """ResuMaker - Automatic summary generator 

Use: main [-options] <num of sentences> <outefile>

Options:

-w <page> Return a summary from text of page web
-p <file> Return a summary from text od a pdf, doc, docx, epb file
-t <file> Return a summary from text of a txt file
-i        To use the program in interactive mode
    """


def save_doc(text, outfile):
    with open(outfile, 'a') as fp:
        fp.write(text)


def option(text, numm, outf):
    if text == 'ERROR':
        print(text)
        return
    text = resumer(text, numm)
    save_doc(text, outf)


def interactive():
    return f'Not implemented yet!'


def main(argv):
    if len(argv) == 5 and argv[1] == '-w':
        text = get_page(argv[2])
        option(text, argv[3], argv[4])
    elif len(argv) == 5 and argv[1] == '-p':
        text = open_doc(argv[2])
        option(text, argv[3], argv[4])
    elif len(argv) == 5 and argv[1] == '-t':
        text = open_Text(argv[2])
        option(text, argv[3], argv[4])
    elif len(argv) == 2 and argv[1] == '-i':
        print(interactive())
    else:
        print(help())


if __name__ == '__main__':
    main(argv)
