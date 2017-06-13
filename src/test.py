# -*- coding:utf-8 -*- 

import trietree_correct_lexicon as trieTree

#注意：
#1. dict.txt文件中如果那行只有空格、或者只有word没词频，都会错误，需注意。
#2. dict.txt文件名可以修改，但是必须放到当前路径下；
#3. 根据dict.txt会生成dict.cache文件，作用是加速加载文件；如果当前目录下存在dict.cache文件，就从该文件中加载数据，反之会生成dict.cache文件。
#4. 在小数据时会导致dict.cache文件比dict.txt文件大。

        
#加载字典
trieTree.trie = trieTree.construction_trietree("lexicon.txt") #("userdic.txt")
if trieTree.trie is not None:
  
    #输出矫正后的word
    word = trieTree.correct_word("mint", 1, trieTree.trie) 
    print (word)





 
 
