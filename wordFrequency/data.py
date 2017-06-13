#coding=utf-8
import codecs

def is_valid_data(img_path, word):
        index1 = img_path.find("_",0)
        index2 = img_path.find("_",index1+1) #len(img_path)-len(word)-5
        word = img_path[index1+1:index2]          
        if word.isalnum(): 
            #if word.isupper() or word.istitle(): #全是大写为true
            word = word.lower() #                                
            return img_path, word
        else:
            return img_path, None
  
def is_chinese(uchar): #判断一个unicode是否是汉字 
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False  

annotation_path = "dict_new.txt"
annotation_path1 = "dict_.txt"
f = codecs.open(annotation_path1, 'w', 'utf-8')

# 只保存汉字的
with codecs.open(annotation_path, 'r', 'utf-8') as ann_file:
    lines = ann_file.readlines()
    #random.shuffle(lines)
    for l in lines:
        img_path, lex = l.strip().split() 
        #print img_path
        #print ("\n")
        #print img_path
        #img_path, lex = is_valid_data(img_path, lex)
        #print img_path
        
        n = 0
        for i in img_path:
            print is_chinese(i)
            if not is_chinese(i):
                n = n+1
  
        if n==len(img_path):
            lst = [img_path, lex]
            l = ' '.join(lst) #用空格重新组合
            print l
            f.write(l)
            f.write("\n")
            
    f.close()