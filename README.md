# Summarization-Using-QA
In our work, we propose a framework to generate summarization by using question answering method. Our method consists of four steps: Firstly, a question generation (QG) model creates a series of questions based on a source text. Secondly, we employ question answering (QA) models to generate answers to these questions using both the
source and the questions. Then a summary generator model generates the summary by considering questions and answers. Lastly, a factuality score (score 1) is calculated based on how consistent the summary is based on the source document. In addition, by another experiment we generate summary directly from the source document without using the QA. This time we calculate factuality score (score 2) and compare this with score 1. We hypothesize that score 1 is bigger than score 2.

## Web application of the System
We created a simple web application to implement the system.
### How to run
- pip install -r requirements.txt
- python app.py

# Demo of our system
![Home Page](https://github.com/SakibBinAlam/Summarization-Using-QA/blob/main/op1.png)
