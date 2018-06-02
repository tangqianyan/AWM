#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: generate_predict.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import codecs
import json
import time

action_question_path = '../intermediate_data/action_question_score'
question_answer_path = '../intermediate_data/question_answer_score'
test_path = '/home/chixiao/dataset/competition/testing_set.txt'
result_path = '../result/result_1'
def find_prediction_for_single_action(question_answer_score_dict,question_related_list):

    answer_return = []
    question_num = len(question_related_list)
    if question_num == 0:
        return [-1 for i in range(100)]
    answer_num = int(100/question_num)
    for question in question_related_list:
        questionId = question[0]
        answer_dict = question_answer_score_dict.get(questionId)
        if answer_dict == None:
            return ['-1']*100
        answer_related_list = sorted(question_answer_score_dict[questionId].items(),key=lambda x:x[1],reverse=True)[:answer_num]
        for v in answer_related_list:
            answer_return.append(v[0][:4]+v[0][-4:])
    answer_return.extend(['-1']*(100-len(answer_return)))
    return answer_return





def generate_prediction():
    print ("Generate Predctions ...")

    with codecs.open(action_question_path,'r','utf8') as f:
        action_question_score_dict = json.load(f)
    print(len(action_question_score_dict))
    with codecs.open(question_answer_path,'r','utf8') as f:
        question_answer_score_dict = json.load(f)


    test_file = open(test_path,'r')
    tmp = 0
    with codecs.open(result_path,'w','utf8') as result_f:
        for line in test_file:
            tmp += 1
            test_Id = line.strip().split('\t')[0]
            question_related = action_question_score_dict.get(test_Id)
            if question_related == None:
                prediction = ['-1'] * 100
            else:
                question_related = sorted(question_related.items(),key=lambda x:x[1],reverse=True)[:10]
                prediction = find_prediction_for_single_action(question_answer_score_dict,question_related)
            result_f.write(','.join(prediction)+'\n')
    test_file.close()
    print(tmp)
    return

if __name__ == "__main__":
    generate_prediction()
