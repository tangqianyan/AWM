#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: map_Q_A.py
#Author: chi xiao
#Mail: 
#Created Time:
############################

import json
import codecs

answer_info_path = "/home/chixiao/dataset/competition/answer_infos.txt"
#answer_info_path = "../sample_data/answer_info_sample"
Q_A_map = "../intermediate_data/Q_A_map"
A_Q_map = "../intermediate_data/A_Q_map"

def map_Q_A():

    """
    find question-answer map, the record should be formalized as :
        {question_id:answers_id1,answer_id2,...}
    find answer-question map, the record should be formalized as :
        {answer: question}
    """
    print("map question answer ...")
    answer_info_fp = open(answer_info_path,'r')
    question_answer_dict = {}
    answer_question_dict = {}
    for line in answer_info_fp:
        line = line.strip().split('\t')
        question_answer_dict.setdefault(line[1],[])
        question_answer_dict[line[1]].append(line[0])

        answer_question_dict.setdefault(line[0],line[1])


    with codecs.open(Q_A_map,'w','utf8') as f:
        json.dump(question_answer_dict,f)

    with codecs.open(A_Q_map,'w','utf8') as f:
        json.dump(answer_question_dict,f)


if __name__=='__main__':
    map_Q_A()



