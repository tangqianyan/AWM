#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: sort_action_question.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import json
import codecs

action_question_path = '../intermediate_data/action_questionId'
question_score_path = '../intermediate_data/question_score'
action_question_score_path = '../intermediate_data/acion_question_score'

answer_score_path = '../intermediate_data/answer_score'
question_answer_map_path = '../intermediate_data/Q_A_map'
question_answer_score_path = '../intermediate_data/question_answer_score'

def compute_question_score(question_info):
    if question_info == None:
        return 0
    score = 0
    for v in question_info[1:]:
        score += int(v)
    #print(score)
    return score


def sort_action_question():

    print("sort action question score")
    with codecs.open(action_question_path,'r','utf8') as f:
        action_question_dict = json.load(f)

    with codecs.open(question_score_path,'r','utf8') as f:
        question_score_dict = json.load(f)

    action_question_score_dict = {}
    for action_id,question_id in action_question_dict.items():
        action_question_score_dict.setdefault(action_id,{})
        for v in question_id['question']:
            question_info = question_score_dict.get(v)
            score = compute_question_score(question_info)
            action_question_score_dict.setdefault(action_id,{}).setdefault(v,score)

    with codecs.open(action_question_score_path,'w','utf8') as f:
        json.dump(action_question_score_dict,f)

    return


def compute_answer_score(answer_score_info):
    if answer_score_info == None:
        return 0

    score = 0
    for v in answer_score_info:
        score += int(v)
    return score


def sort_question_answer():

    print("sort question answer ...")
    with codecs.open(question_answer_map_path,'r','utf8') as f:
        q_a_map_dict = json.load(f)

    with codecs.open(answer_score_path,'r','utf8') as f:
        answer_score_dict = json.load(f)

    question_answer_score_dict = {}
    for q_id , a_list in q_a_map_dict.items():
        for v in a_list:
            answer_score_info = answer_score_dict[v]
            score = compute_answer_score(answer_score_info)
            question_answer_score_dict.setdefault(q_id,{}).setdefault(v,score)

    with codecs.open(question_answer_score_path,'w','utf8') as f:
        json.dump(question_answer_score_dict,f)

    return







if __name__ =="__main__":
    sort_action_question()
    #sort_question_answer()

