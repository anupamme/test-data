import json
import sys
import os
from random import randint
import re

'''
Algo: start from the root directory.
2. Do depth first search and when there is no further directory, count the number of files and at random read 1/10th of files and in each file read at random 1/10 of lines.
3. Output the lines as a json in output file
'''

def getListOfFiles(root_dir, file_list):
    print 'root dir: ' + root_dir
    list_dir = os.listdir(root_dir)
    for local_dir in list_dir:
        print 'local dir: ' + local_dir
        path = os.path.join(root_dir, local_dir)
        print 'path: ' + path
        if os.path.isdir(path):
            getListOfFiles(path, file_list)
        else:
            file_list.append(path)

if __name__=="__main__":
    root_dir = sys.argv[1]
    file_list= []
    getListOfFiles(root_dir, file_list)
    length_file = len(file_list)
    result_text= []
    for local_file in file_list:
        try:
            data = json.loads(open(local_file, 'r').read())
        except ValueError:
            print 'No json object found in: ' + local_file
            continue
        if 'review' in data:
            review_arr = re.split('\n|\.', data['review'])
            result_text = result_text + review_arr
    f = open('aggregate.json', 'w')
    f.write(json.dumps(result_text))
    f.close()
    output_length = int(sys.argv[2])
    total_length = len(result_text)
    filtered_result = []
    count = 0
    while count < output_length:
        index = randint(0,total_length)
        filtered_result.append(result_text[index])
        count += 1
    f = open('result.json', 'w')
    f.write(json.dumps(filtered_result))
    f.close()
             
            
        