#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: statis.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import codecs
import json
import numpy as np
from matplotlib import pyplot as plt

action_questionId_path = "../intermediate_data/action_questionId"
stat_interval_path = "../statis_data/interval"

def stat_action_info():
    """
    find data distribution
    """
    with codecs.open(action_questionId_path,'r','utf8') as fid:
        action_question_answer = json.load(fid)

    question_num = [[len(set(v['question'])),len(set(v['answer']))] for k,v in action_question_answer.items()]
    question_num = np.matrix(question_num)
    print (question_num)
    return question_num


def stat_question_set_info():
    """
    find data distribution
    """
    with codecs.open(action_questionId_path,'r','utf8') as fid:
        action_question_answer = json.load(fid)

    question_set = set([])
    answer_set = set([])
    for k,v in action_question_answer.items():
        question_set = question_set | set(v['question'])
        answer_set = answer_set | set(v['answer'])
    return len(question_num),len(answer_set)


def stat_interval(my_list,name,interval=20):
    #interval_list = [i for i in range(0,np.max(my_list)+interval,interval)]
    sum_list = [0] * int((np.max(my_list)+interval)/interval)
    for v in my_list:
        sum_list[int(v[0]/interval)] += 1
    with codecs.open(stat_interval_path+name+str(interval),'w','utf8') as f:
        for i in range(len(sum_list)):
            f.write(str((i+1)*interval)+ " : " + str(sum_list[i]) + '\n')

    return sum_list



def draw_hist(my_list,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(my_list,100)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()

