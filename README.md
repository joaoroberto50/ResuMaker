# ResuMaker
This is a simple project that makes small summaries of texts.

Using the nltk module, you can open documents in different formats, and nltk will do natural language processing, finding the main sentences and returning a summary with the main ones found.

## How to use
Install the requeriments in you venv
```
pip install requeriments.txt
```
Now, open python interpreter
```
$ python
>>> import nltk
>>> nltk.download('punkt')
>>> ntlk.download('stopwords')
```
Now ready to use
```
python main [options] <filename> numm <outfile>
```
[options]    - type of file you will open

'<filename>' - name of file to do a summary
  
numm         - number of sentences you want in the summary

'<outfile>'  - name of a txt file to save the generated summary
  
Use the Help guide
```
python main -h
```

