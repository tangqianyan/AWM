#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: find_question_from_test.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import codecs
import json


actionRecords_path = "/home/chixiao/dataset/competition/testing_set.txt"
#actionRecords_path = "../sample_data/test_set_sample"
actionQuestionId_path = "../intermediate_data/action_questionId"

answerId_path = "/home/chixiao/dataset/competition/answer_id.dict"
questionId_path = "/home/chixiao/dataset/competition/question_id.dict"
A_Q_map_path = "../intermediate_data/A_Q_map"


def read_answer_question_dict():
    print("read answer question dict ...")
    answerId_dict = {}
    questionId_dict = {}

    for line in open(answerId_path):
        line = line.strip().split('\t')
        answerId_dict.setdefault(line[0],line[1])

    for line in open(questionId_path):
        line = line.strip().split('\t')
        questionId_dict.setdefault(line[0],line[1])
    return answerId_dict,questionId_dict

def read_A_Q_map():
    print("read answer question map ...")

    with codecs.open(A_Q_map_path,'r','utf8') as f:
        A_Q_map_dict = json.load(f)
    return A_Q_map_dict


def find_questionId_from_record():

    """
    find the questions' OR answer' ID from the users' actions.
    """
    print("find questionId from the action records ...")

    fp = open(actionRecords_path,'r')
    answer_dict,question_dict = read_answer_question_dict()
    A_Q_map_dict = read_A_Q_map()

    action_questionId_dict = {}
    tmp_num = 0
    for line in fp:
        line = line.strip().split('\t')
        action_questionId_dict.setdefault(line[0],{'question':[],'answer':[]})
        tmp_num +=1
        if int(line[1]) > 0:
            actions = line[2].split(',')
            for v in actions:
                v = v.split('|')
                if int(v[2]) != 0:
                    Id = 0
                    if v[0][0] =='A':
                        Id = answer_dict[v[0][1:]]
                        action_questionId_dict[line[0]]['answer'].append(Id)
                        action_questionId_dict[line[0]]['question'].append(A_Q_map_dict[Id])
                    elif v[0][0] == 'Q':
                        Id = question_dict.get(v[0][1:])
                        action_questionId_dict[line[0]]['question'].append(Id)
    with codecs.open(actionQuestionId_path,'w','utf8') as f:
        json.dump(action_questionId_dict,f)
    print(len(action_questionId_dict))
    print(tmp_num)
    return
if __name__ == "__main__":
    find_questionId_from_record()
