#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: count_Q_A.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import json
import codecs

#question_info_path = '../sample_data/question_info_sample'
question_info_path = '/home/chixiao/dataset/competition/question_infos.txt'
question_score_path = '../intermediate_data/question_score'

#answer_info_path = '../sample_data/answer_info_sample'
answer_info_path = '/home/chixiao/dataset/competition/answer_infos.txt'
answer_score_path = '../intermediate_data/answer_score'


def compute_question_score():

    fp = open(question_info_path)
    question_score_dict = {}

    for line in fp:
        line = line.strip().split('\t')
        question_score_dict.setdefault(line[0],line[1:6])

    with codecs.open(question_score_path,'w','utf8') as fid:
        json.dump(question_score_dict,fid)

    return

def compute_answer_score():

    fp = open(answer_info_path)
    answer_score_dict = {}

    for line in fp:
        line = line.strip().split('\t')
        answer_score_dict.setdefault(line[0],[line[4],line[9],line[10],line[11],line[12]])

    with codecs.open(answer_score_path,'w','utf8') as fid:
        json.dump(answer_score_dict,fid)

    return

if __name__=="__main__":
    #compute_question_score()
    compute_answer_score()
