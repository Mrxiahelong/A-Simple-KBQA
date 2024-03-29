import numpy as np
vocab=np.load('.//entity//vocab.npy')
tag=np.load('.//entity//Tags.npy')
max_seq_length=150
word2int={v:k for k,v in enumerate(vocab)}
int2word={k:v for k,v in enumerate(vocab)}
ids2tag={k:v for k,v in enumerate(tag)}
tag2ids={v:k for k,v in enumerate(tag)}


entity_type=['影视作品','书籍','歌曲','人物','企业','网络小说','生物']
relation_type=['主演','作者','歌手','出生日期','导演','出生地','出版社','成立日期','连载网站','国籍','毕业院校','民族','所属专辑','目','作曲']

entity_relation_map={'影视作品':'这部剧','书籍':'这本书','歌曲':'这首歌','人物':'他','企业':'这公司','生物':'这生物','网络小说':'这小说'}

yitu=['谁主演的这部剧?','这部剧是谁主演的?','这部剧的主演是谁?','这部剧的演员是谁?','哪个演员演的这部剧?','这部剧是谁拍摄的?','谁拍摄的这部剧?',
     '这本书是谁写的?','谁写的这本书?','这本书是谁编写的?','谁编写的这本书?','谁是这本书的作者?','这本书是谁写的?','谁写的这本书?','这本书的作者是谁?',
     '谁唱的这首歌?','这首歌是谁唱的?','谁是这首歌的歌手?','这首歌的歌手是谁?','他出生于多久?','他多久出生的?','他的生日是多久?','谁执导的这电影','电影的导演是谁?','谁导演的这电影',
     '他出生在哪?','他的出生地在哪?','哪里是他的出生地?','他在哪出生的?','这本书的出版社是哪个?','哪个出版社是这本书的出版社?','这小说的连载网站是哪个网站?','哪个网站连载这小说','这小说连载在哪里?',
     '他是哪个国家的?','哪个国家是他的祖国?','他是哪个国籍的?','他毕业于那个学校?','哪个学校是他的母校?','他的毕业学校是哪个?','哪个学校是他毕业的学校?','他是哪个民族的?','他现在是哪个民族的?','这首歌所属于哪个专辑?','哪个专辑有这首歌?',
     '这生物是哪个科目的?','这生物是啥?','这是啥生物?','谁是这首歌的作曲?','这首歌的作曲是谁?','这公司成立于多久?','多久成立的这公司?']
y=['主演','主演','主演','主演','主演','主演','主演','作者','作者','作者','作者','作者','作者','作者','作者','歌手','歌手','歌手','歌手',
  '出生日期','出生日期','出生日期','导演','导演','导演','出生地','出生地','出生地','出生地','出版社','出版社','连载网站','连载网站','连载网站','国籍','国籍','国籍',
  '毕业院校','毕业院校','毕业院校','毕业院校','民族','民族','所属专辑','所属专辑','目','目','目','作曲','作曲','成立日期','成立日期']