#!/usr/bin/python
# _*_ coding: utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
'''
王者荣耀的段位分布
'''
import MySQLdb
import sys
import random
import matplotlib.pyplot as plt



class Duanwei(object):
    def __init__(self,renshu=1000,cishu=10000):
        self.renshu = renshu
        self.cishu = cishu
        self.xunhuan = cishu

    def beginning(self):
        self.x = range(0, self.renshu)
        self.y = {}
        for i in self.x:
            self.y[i] = 1

    def dbbeginning(self):
        sql_creat = '''CREATE TABLE G%dren%dci (
          `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
          `player1` int(11) DEFAULT NULL,
          `player2` int(11) DEFAULT NULL,
          `player3` int(11) DEFAULT NULL,
          `player4` int(11) DEFAULT NULL,
          `player5` int(11) DEFAULT NULL,
          `score` int(11) DEFAULT NULL,
          `times` int(11) DEFAULT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;''' % (self.renshu,self.cishu)
        self.cursor.execute(sql_creat)
        self.conn.commit()

    def random_play(self):
        while self.xunhuan >= 1:
#            t = [random.randint(0, (self.renshu-1)) for i in range(0, 10)]    可能取到重复数字，
            self.t_x = random.sample(self.x, 10)
            t = random.sample(self.x, 10)
            w = t[0:5]
            l = t[5:10]
            for key in w:
                self.y[key] += 1
            for key in l:
                if self.y[key] == 0:
                    pass
                else:
                    self.y[key] -= 1
            sql_w = '''INSERT INTO G%dren%dci (player1,player2,player3,player4,player5,score,times) \
                        VALUES(%d,%d,%d,%d,%d,%d,%d)''' % \
                    (self.renshu, self.cishu, w[0], w[1], w[2], w[3], w[4], 1, self.cishu-self.xunhuan+1)
            sql_l = '''INSERT INTO G%dren%dci (player1,player2,player3,player4,player5,score,times) \
                        VALUES(%d,%d,%d,%d,%d,%d,%d)''' % \
                    (self.renshu, self.cishu, l[0], l[1], l[2], l[3], l[4], -1, self.cishu-self.xunhuan+1)
            self.cursor.execute(sql_w)
            self.cursor.execute(sql_l)
            self.conn.commit()
            self.xunhuan -= 1
        self.cursor.close
        self.conn.close

    def tongji(self):
        self.qingtong = 0
        self.baiyin = 0
        self.huangjin = 0
        self.baijin = 0
        self.zuanshi = 0
        self.heiyao = 0
        self.wangzhe = 0
        for key,value in self.y.items():
            if value <= 9:
                self.qingtong += 1
            elif value <= 18:
                self.baiyin += 1
            elif value <= 34:
                self.huangjin += 1
            elif value <= 50:
                self.baijin += 1
            elif value <= 75:
                self.zuanshi += 1
            elif value <= 100:
                self.heiyao += 1
            elif value > 100:
                self.wangzhe += 1
            else:
                pass
        self.jieguo = (self.qingtong,self.baiyin,self.huangjin,self.baijin,self.zuanshi,self.heiyao,self.wangzhe)

    def conn_mysql(self):
        self.conn = MySQLdb.Connect(
        #host = 'localhost',
        #port = 3306,
        user = 'root',
        passwd = '',
        db = 'wangzhe',
        charset = 'utf8'
        )
        self.cursor = self.conn.cursor()

    def pic(self):
        fig1 = plt.figure(3)
        rects = plt.bar(left=(9/2,18/2,34/2,50/2,75/2,100/2,70),\
                height=(self.qingtong,self.baiyin,self.huangjin,self.baijin,self.zuanshi,self.heiyao,self.wangzhe),\
                        color=('r'),width=5, align="center", yerr=0.000001)
        # left表示直方图的开始的位置（也就是最左边的地方），height是指直方图的高度，当直方图太粗时，可以通过width来定义直方图的宽度
        # 注意多个直方图要用元组，yerr这个参数是防止直方图触顶。
        title = "Ranking Distrubution of %dpeople after%dbattles"%(self.renshu,self.cishu)

        plt.title(title)

        def autolable(rects):
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2., 1.03 * height, '%s' % float(height))

        autolable(rects)
        plt.xticks((9/2,18/2,34/2,50/2,75/2,100/2,70), (u'青铜', u'白银', u'黄金',u'铂金',u'钻石',u'星曜',u'王者'))
        plt.show()


if __name__ == '__main__':
   t1 = Duanwei(111,111)
   t1.beginning()
   t1.conn_mysql()
   t1.dbbeginning()
   t1.random_play()
   t1.tongji()
   t1.pic()
   print t1.jieguo
   print t1.t_x
