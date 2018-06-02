#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: extract_records.py
#Author: chi xiao
#Mail: 
#Created Time:
############################
import sys
import re
import getopt

def sample_data(f_source,f_target,line_num,method):
    print("sample data ...")
    fptr_source = open(f_source,'r')
    fptr_target = open(f_target,'w')
    tmp = 0
    if method == 'head':
        while True:
            for line in fptr_source:
                fptr_target.write(line)
                tmp += 1
                if tmp >= line_num:
                    return
        #for line in fptr_source.readlines()[:line_num]:
        #    fptr_target.write(line)
    elif method == 'tail':
        for line in fptr_source.readlines()[-line_num:]:
            fptr_target.write(line)
    fptr_target.close()
    fptr_source.close()
    return


def usage():
    print(
        '''
          sample data from a big file to generate a small example.

          ./extract_records.py --method <method> --source <source_file> --target_file <target_file>
          or for short version,
          ./extract_records.py -m <method> -s <source_file> -t <target_file>

          method|-m: head or tail, sample data from the file in the head/tail
          '''
    )
    return 

if __name__ == "__main__":

    method = ''
    source_file = ''
    target_file = ''
    try:
        if len(sys.argv) <= 1:
            sys.exit(0)
        options, args = getopt.getopt(sys.argv[1:],"hm:n:s:t:",["help","method=","num=","source=","target="])
        for k,v in options:
            if k in ('-h','--help'):
                usage()
                sys.exit(0)
            if k in ('-m','--method'):
                method = v
                assert method in ('head','tail')
            if k in ('-n','--num'):
                line_num = int(v)
            if k in ("-s","--source"):
                source_file = v
            if k in ("-t","--target"):
                target_file = v
        assert source_file != '' and target_file != ''
    except Exception, e:
        print(e)
        sys.exit(1)
    if  method == 'head':
        sample_data(source_file,target_file,line_num,method)
    if method == "tail":
        sample_data(source_file,target_file,line_num,method)

    sys.exit(0)



