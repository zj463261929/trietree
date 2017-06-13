#coding=utf-8
import jieba 
from collections import Counter
import codecs 

stopword_path = r'stopwords.dat'
class seg_word(object):
	def __init__(self, inputpath, outputpath):
		self.inputpath = inputpath
		self.outputpath = outputpath

	def cut_data(self):
		with codecs.open(inputpath, 'r', 'utf-8') as fr:
			res = jieba.cut(fr.read())
		return res

	def output_file(self):
		outcome = self.cumpute_word_count()
		with codecs.open(outputpath, 'w', 'utf-8') as fw:
			for k,v in outcome.items():
				fw.write(k + ' ' + str(v) + '\n')

	def filter_data(self):
		with codecs.open(stopword_path,'r','utf-8') as f:
			stopword_list = f.read()
		seg_res = self.cut_data()
		res_list = [word.strip() for word in seg_res if word not in stopword_list] #strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
		return res_list

	def cumpute_word_count(self):
		res_word = self.filter_data()
		word_freq = dict(Counter(res_word))
		return word_freq
	
	def get_cut_data(self):
		with codecs.open(stopword_path,'r','utf-8') as f:
			stopword_list = f.read()
		seg_res = self.cut_data()
		res_list = [word.strip() for word in seg_res if word not in stopword_list] #strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
		
		with codecs.open(outputpath, 'w', 'utf-8') as fw:
			n = 0
			for i in range(len(res_list)):
				if n%20 == 0:
					fw.write(res_list[i] + " " + '\n')
				else:
					fw.write(res_list[i] + " ")
				n = n + 1
						
	def is_chinese(self, uchar): #判断一个unicode是否是汉字  例如：uchar = \u4e00
		if uchar.find("\u", 0) > -1:
			uchar = uchar[2:] #4e00
			#print uchar
			uchar = int(uchar,16) #转成10进制，4e00->19968   9fa5->40869
			if uchar >= 19968 and uchar<=40869:#if uchar >= u'\u4e00' and uchar<=u'\u9fa5':		
				return True
			else:
				return False
		
	def cut_word(self):
		outcome = self.cumpute_word_count()
		lst = []
		with codecs.open(outputpath, 'w', 'utf-8') as fw:
			n = 3
			for c in range(10): #写数字0-9
				fw.write(str(c) + ' ' + str(n) + '\n')
				n = n + 1
			
			for c in range(26): #写字母a-z
				c = c + 97  #97->a  122->z
				fw.write(chr(c) + ' ' + str(n) + '\n')
				n = n + 1
				
			
			for k,v in outcome.items():
				for c in k:
					lst.append(c)
					
			lst = list(set(lst))#list(set(lst)) 去除列表中重复的元素
			for c in lst: 
				cc = c.encode("raw_unicode_escape")
				#print "\n"
				#print cc
				if self.is_chinese(cc):
					fw.write(c + ' ' + str(n) + '\n')
					n = n + 1
			print ("dict count:{}\n".format(n))
			
	def cut_word_new(self):
		words = []
		with codecs.open("/opt/ligang/data/pic2000_15_data_2017_5_31/result_img_word/WordBBText_new.txt", 'rb', "utf-8") as ann_file:
			lines = ann_file.readlines()
			for l in lines:
				lst = l.strip().split() 
				if len(lst) > 1:
					for c in lst[1]:
						words.append(c)
					
		lst = list(set(words)) #去重复的
		#lst.sort()
		#print (len(lst))
		fw =  codecs.open("/opt/zhangjing/ocr/Attention-OCR-new-version/word_label_new.txt", 'w', "utf-8")
		c_words = []
		n = 3
		for c in range(10): #写数字0-9
			fw.write(str(c) + ' ' + str(n) + '\n')
			n = n + 1
			
		for c in range(26): #写字母a-z
			c = c + 97  #97->a  122->z
			fw.write(chr(c) + ' ' + str(n) + '\n')
			n = n + 1
				
			
		for c in lst: 
			cc = c.encode("raw_unicode_escape")
			#print "\n"
			#print cc
			if self.is_chinese(cc):
				fw.write(c + ' ' + str(n) + '\n')
				n = n + 1
		print ("dict count:{}\n".format(n))	
			
			
			
	def val_word(self):
		lst = []
		with codecs.open(outputpath, 'r', 'utf-8') as fr:
			lines = fr.readlines()
			for l in lines:
				word, index1 = l.strip().split() 
				lst.append(word)
		n = 0
		for c in lst:
			if lst.count(c)>1:
				n = n + 1
				
		print ("repeat word num:{}\n".format(n-1))
		
			
			
if __name__ == '__main__':
	inputpath = r'newsgroup.txt'
	outputpath = r'dict11.txt'
	c = seg_word(inputpath, outputpath)
	#res = c.output_file() #从语料库txt中分词及统计词频
	#res = c.get_cut_data() #从语料库txt中 只分词，每行存储20个词
	#res = c.cut_word() #从语料库中，切分成一个个字，去重，加label(从3开始)
	res = c.cut_word_new() #从样本集的文档中对对个字重新进行编码，label(从3开始)
	#res = c.val_word() #验证word_label.txt中字是否有重复
