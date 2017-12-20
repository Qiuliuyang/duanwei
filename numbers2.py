# !usr/bin/python
# _*_ coding:utf-8 _*_
# __author__ = "Qiu"
# Email = "qiu@immunet.cn"
class change4(object):
    def __init__(self,number=100):
        self.l = list(str(number))
        self.c = len(self.l)
        self.n1 = int(self.l[0])
        self.n2 = int(self.l[1])
        self.n3 = int(self.l[2])
        self.n4 = int(self.l[3])

class change5(object):
    def __init__(self,number=100):
        self.l = list(str(number))
        self.c = len(self.l)
        self.n1 = int(self.l[0])
        self.n2 = int(self.l[1])
        self.n3 = int(self.l[2])
        self.n4 = int(self.l[3])
        self.n5 = int(self.l[4])

class ss41(object):
    def __init__(self,ss='send'):
        self.l = list(ss)
        self.c = len(self.l)
        self.n1 = self.l[0]
        self.n2 = self.l[1]
        self.n3 = self.l[2]
        self.n4 = self.l[3]

class ss42(object):
    def __init__(self,ss='send'):
        self.l = list(ss)
        self.c = len(self.l)
        self.n1 = self.l[0]
        self.n2 = self.l[1]
        self.n3 = self.l[2]
        self.n4 = self.l[3]

class ss5(object):
    def __init__(self,ss='money'):
        self.l = list(ss)
        self.c = len(self.l)
        self.n1 = self.l[0]
        self.n2 = self.l[1]
        self.n3 = self.l[2]
        self.n4 = self.l[3]
        self.n5 = self.l[4]

class jisuan(object):
    def __init__(self,l1='send',l2='more',l3='money'):
        self.l1 = list(l1)
        self.l2 = list(l2)
        self.l3 = list(l3)

def method():
    l = range(10)
    l2 = range(1, 10)
    for ss41.n1 in l2:
        for ss42.n1 in l2:
            if ss41.n1 + ss42.n1 > 9:
                for ss41.n2 in l:
                    for ss41.n3 in l:
                        for ss41.n4 in l:
                            for ss42.n2 in l:
                                for ss42.n3 in l:
                                    for ss42.n4 in l:
                                        for ss5.n1 in l2:
                                            for ss5.n2 in l:
                                                for ss5.n2 in l:
                                                    for ss5.n3 in l:
                                                        for ss5.n4 in l:
                                                            for ss5.n5 in l:
                                                                t1 = ss41.n1*1000 + ss41.n2*100 + ss41.n3*10 + ss41.n4
                                                                t2 = ss42.n1*1000 + ss41.n2*100 + ss41.n3*10 + ss41.n4
                                                                t3 = ss5.n1*10000 + ss5.n2*0100 + ss5.n3*100 +\
                                                                     ss5.n4*10+ss5.n5
                                                                if t1 + t2 == t3:
                                                                    total = set([ss41.n1,ss41.n2,ss41.n3,ss41.n4,\
                                                                        ss42.n1,ss42.n2,ss42.n3,ss42.n4,\
                                                                                ss5.n1,ss5.n2,ss5.n3,ss5.n4,ss5.n5])
                                                                    if len(total) == 8:
                                                                        print ("%d,%d,%d" % (t1, t2, t3))


if __name__ == '__main__':

    n1 = ss41('send')
    n2 = ss42('more')
    n3 = ss5('money')
    zimu = set([ss41.n1,ss41.n2,ss41.n3,ss41.n4,\ss42.n1,ss42.n2,ss42.n3,ss42.n4,\ss5.n1,ss5.n2,ss5.n3,ss5.n4,ss5.n5])
    method()
