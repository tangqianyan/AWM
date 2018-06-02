#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: Answer.py
#Author: chi xiao
#Mail: 
#Created Time:
############################

import codecs
import json

class Answer():
    """
    descriptions of class
    """
    __whole_data = {}


    def __init__(self,AnswerId,QuestionId,AnswerId,QuestionId,IsAnonymous,AuthorId,IsGood,IsRecommend,CreateTime,ExtGraph,ExtVideo,
                ThankNum,AgreeNum,CommentNum,CollectNum,OpposeNum,ReportNum,NohelpNum,Text,TopicIds):
        self.AnswerId = AnswerId
        self.QuestionId = QuestionId
        self.IsAnonymous = IsAnonymous
        self.AuthorId = AuthorId
        self.IsGood = IsGood
        self.IsRecommend = IsRecommend
        self.CreateTime = CreateTime
        self.ExtGraph = ExtGraph
        self.ExtVideo = ExtVideo
        self.ThankNum = ThankNum
        self.AgreeNum = AgreeNum
        self.CommentNum = CommentNum
        self.CollectNum = CollectNum
        self.OpposeNum = OpposeNum
        self.ReportNum = ReportNum
        self.NohelpNum =NohelpNum
        self.Text = Text
        self.TopicIds =TopicIds

        self.Score = 0

    def getAnswerById(id):
        if not (Id in Answer.__whole_data):
            Answer.__whole_data[id] = Answer(id)
        return Answer.__whole_data[id]

    def computeScore(id):
        ans = Answer.__whole_data[id]
        ans.Score = ans.ThankNum
        return ans.Score


