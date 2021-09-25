import torch
from transformers import pipeline

summarizer = pipeline("summarization")

def model_forward(article): 
    summary =''
    if (len(article)>1024):
        for i in range (0,int(len(article)/1024)-1):
            if (i== int(len(article)/1024)-1):
              summ =summarizer(article[1024*(i):], max_length=100, min_length=3, do_sample=False)[0]    
            else:
              summ =summarizer(article[1024*(i):1024*(i+1)], max_length=100, min_length=3, do_sample=False)[0]
            summary += ''+summ['summary_text']
            #print(summary['summary_text'])
    else:
        summary =  summarizer(article[:], max_length=100, min_length=3  , do_sample=False)[0]['summary_text']
    return summary
    