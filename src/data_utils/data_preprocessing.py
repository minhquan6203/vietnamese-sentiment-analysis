
import py_vncorenlp
import pandas as pd
import os
py_vncorenlp.download_model(save_dir='/content')
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='/content')

sign=[',', '.', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '<', '>', '"', "'", 
      '`', '...', '--', '-', '_', '*', '@', '#', '$', '%', '^', '&', '+', '=', '/', '\\', 
      '|', '~', '``', "''", '“', '”', '‘', '’', '«', '»', '„', '‟', '‹', '›', '〝', '〞', 
      '‒', '–', '—', '―',    '•', '·', '⋅', '°',':3','<3',':>',':v',':)','=)',':(','-.-','-_-']

word_seg=True

def xoa_trung_lap(s):
    loop = ""
    i=1
    while i <= len(s)-1:
      if s[i]==s[i-1] and (i==len(s)-1 or s[i+1]==' '):
        j=i
        loop=s[i]
        while s[j-1] == s[j]:
          loop+=s[j]
          j-=1
        s = s.replace(loop, s[i])
      i+=1
    return s
  
def scanerr(sentence,word_seg=False):
    for t in sign:
        sentence=sentence.lower().replace(t,'')
    sentence=xoa_trung_lap(sentence)
    if ('meow' in sentence or 'babe' in sentence or 'người yêu'  in sentence or 'ahihi'  in sentence 
        or 'sút vào'  in sentence or sentence == 'không' or sentence == 'không có' or 'bồ' in sentence 
        or 'vô địch' in sentence or 'geng' in sentence or 'đồng hồ' in sentence or 'cuồng phong' in sentence 
        or 'ngủ sớm' in sentence  or 'ván bài' in sentence or 'không có ý kiến gì' in sentence or 
        'khong co gi ca' in sentence  or 'sinh năm 98'  in sentence or 'té xe'  in sentence or 'liên quân'  in sentence 
        or 'using'  in sentence or 'pizza'  in sentence or 'bitis'  in sentence or 'bắt được em'  in sentence 
        or 'mi đắng'  in sentence or 'tiếng pháo hoa'  in sentence or "tới bên em" in sentence):
            sentence = 'bình thường'
    if word_seg:
        return rdrsegmenter.word_segment(sentence)
    else:
        return sentence

def main():
  train=pd.read_csv('/content/vietnamese-sentiment-analysis/data/train.csv')
  dev=pd.read_csv('/content/vietnamese-sentiment-analysis/data/dev.csv')
  test=pd.read_csv('/content/vietnamese-sentiment-analysis/data/test.csv')
  word_seg=False

  for i in range(len(train)):
        train['sentence'][i]=scanerr(train['sentence'][i],word_seg)[0]
  for i in range(len(dev)):
    dev['sentence'][i]=scanerr(dev['sentence'][i],word_seg)[0]
  for i in range(len(test)):
    test['sentence'][i]=scanerr(test['sentence'][i],word_seg)[0]

  train.to_csv('/content/vietnamese-sentiment-analysis/data/train_new.csv')
  dev.to_csv('/content/vietnamese-sentiment-analysis/data/dev_new.csv')
  test.to_csv('/content/vietnamese-sentiment-analysis/data/test_new.csv')

if __name__ == '__main__':
    main()
    
