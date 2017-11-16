import sys,pypinyin,eyed3

reload(sys)  
sys.setdefaultencoding('utf8')
import os

base=r'/mnt/winD/BaiduYunDownload/pinyintest'
tag=['.mp3','.MP3','.FLAC','flac','.APE']

   

a=[]
def modifytag(filename,*attr):
	if len(attr)==None:
		print('no attr given ,please input "artist","title" ...')
		quit()
	else:
		audiofile=eyed3.load(filename)
		for changeattr in attr:
			pinyinattr=pypinyin.lazy_pinyin(getattr(audiofile.tag,changeattr))
			pinyinattr=''.join(str(x) for x in pinyinattr)
			setattr(audiofile.tag,changeattr,pinyinattr.decode('utf-8'))
		audiofile.tag.save()

def getmp3(root,label):
    base_list = [os.path.normcase(i) for i in os.listdir(root) if  i !='System Volume Information' ]
    for i in base_list:
        p=os.path.isdir(os.path.join(root,i))

        if p:
            getmp3(os.path.join(root,i),label)
        else:
            if os.path.splitext(i)[1] in label:
                a.append(os.path.join(root,i))
getmp3(base,tag)
for b in a:
	modifytag(b,'title','artist','album','album_artist')
