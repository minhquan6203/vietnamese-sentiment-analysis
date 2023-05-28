
import py_vncorenlp

py_vncorenlp.download_model(save_dir='/content')
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='/content')

sign=[',', '.', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '<', '>', '"', "'", 
      '`', '...', '--', '-', '_', '*', '@', '#', '$', '%', '^', '&', '+', '=', '/', '\\', 
      '|', '~', '``', "''", '“', '”', '‘', '’', '«', '»', '„', '‟', '‹', '›', '〝', '〞', 
      '‒', '–', '—', '―',    '•', '·', '⋅', '°',':3','<3',':>',':v',':)','=)',':(','-.-','-_-']


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
     
def scanerr(sentence):
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

    return rdrsegmenter.word_segment(sentence)


