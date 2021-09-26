
from transformers import pipeline

summarizer = pipeline("summarization", model= 't5-small', tokenizer= 't5-small' )

def model_forward(article): 
    summary =''
    max_input_length = summarizer.tokenizer.model_max_length
    if (len(article)>max_input_length):
        for i in range (0,int(len(article)/max_input_length)-1):
            if (i== int(len(article)/max_input_length)-1):
              summ =summarizer(article[max_input_length*(i):], max_length=int(len(article[max_input_length*(i):])*1/2), min_length=3, do_sample=False)[0]    
            else:
              summ =summarizer(article[max_input_length*(i):max_input_length*(i+1)], max_length=int(len(article[max_input_length*(i):max_input_length*(i+1)])*1/2), min_length=3, do_sample=False)[0]
            summary += ''+summ['summary_text']
            #print(summary['summary_text'])
    else:
        summary =  summarizer(article[:], max_length=int(len(article[:])*1/2), min_length=3  , do_sample=False)[0]['summary_text']
    return summary
    