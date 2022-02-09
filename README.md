# Stylometry

This library is a fork from https://github.com/jpotts18/stylometry updated to Python 3 and growing from there.

## Installation
```bash
$ git clone https://github.com/pendrag/stylometry.git
$ cd stylometry
$ pip install -r requirements.txt
$ python setup.py install
```
## Test it

```python
from stylometry.extract import *
text = StyloDocument('stylometry/data/TheWould-enDoor.txt')
text.text_output()
```
Output:
```
##############################################

Name: 

>>> Phraseology Analysis <<<

Lexical diversity        :
Mean Word Length         :
Mean Sentence Length     :
STDEV Sentence Length    :
Mean paragraph Length    :
Document Length          :

>>> Punctuation Analysis (per 1000 tokens) <<<

Commas                   : 31.27585636273374
Semicolons               : 0.4137018037398643
Quotations               : 0.0
Exclamations             : 1.0066743891003365
Colons                   : 0.04137018037398643
Hyphens                  : 0.0
Double Hyphens           : 0.0

>>> Lexical Usage Analysis (per 1000 tokens) <<<

and                      : 23.084560648684427
but                      : 4.785150863257764
however                  : 0.013790060124662143
if                       : 1.4893264934635115
that                     : 6.412377957967896
more                     : 1.8616581168293893
must                     : 0.7170831264824314
might                    : 0.20685090186993216
this                     : 4.137018037398643
very                     : 0.9377240884770257
```
