#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:58:15 2020

@author: conniemessi
"""


# 'Convict' 'Marry' 'Elect' 'Start-Org' 'Start-Position'

import json

with open('test.json', 'r') as f:
    data = json.load(f)
    
#base_event_type = ['Justice:Convict', 'Life:Marry', 'Personnel:Elect', 'Business:Start-Org', 'Personnel:Start-Position']
base_event_type = ['Justice:Convict', 'Life:Marry', 'Personnel:Elect', 'Business:Start-Org', 'Personnel:Start-Position',
                   'Conflict:Demonstrate', 'Justice:Arrest-Jail', 'Justice:Release-Parole', 'Justice:Trial-Hearing', 'Life:Injure']

new_test = []
    
event_type_list = []
for i in range(len(data)):
    sentence = data[i]
    
    if(sentence['golden-event-mentions']!=[]):
        event_type = sentence['golden-event-mentions'][0]['event_type']
        
        for j in base_event_type:
            if(event_type==j):
                new_test.append(sentence)
                continue
    
        event_type_list.append(event_type)
        
all_event_type = list(set(event_type_list))
train_event_type = list(set(all_event_type) - set(base_event_type))

# Serializing json  
json_object = json.dumps(new_test, indent = 4) 
  
# Writing to sample.json 
with open("10way_test_ft.json", "w") as outfile: 
    outfile.write(json_object) 



# ------ k shot train -------
with open('train.json', 'r') as f:
    data = json.load(f)
    
#todo: change the k shot
k = 10

# list1,list2,list3,list4,list5 = [],[],[],[],[]
list1,list2,list3,list4,list5,list6,list7,list8,list9,list10 = [],[],[],[],[],[],[],[],[],[]

for i in range(len(data)):
    sentence = data[i]
    
    if(sentence['golden-event-mentions']!=[]):
        event_type = sentence['golden-event-mentions'][0]['event_type']
        if(event_type == base_event_type[0]):
            list1.append(sentence)
        if(event_type == base_event_type[1]):
            list2.append(sentence)
        if(event_type == base_event_type[2]):
            list3.append(sentence)
        if(event_type == base_event_type[3]):
            list4.append(sentence)
        if(event_type == base_event_type[4]):
            list5.append(sentence)
        if(event_type == base_event_type[5]):
            list6.append(sentence)
        if(event_type == base_event_type[6]):
            list7.append(sentence)
        if(event_type == base_event_type[7]):
            list8.append(sentence)
        if(event_type == base_event_type[8]):
            list9.append(sentence)
        if(event_type == base_event_type[9]):
            list10.append(sentence)

k_shot_new_train = []   
      
k_shot_new_train.append(list1[:k])
k_shot_new_train.append(list2[:k])
k_shot_new_train.append(list3[:k])
k_shot_new_train.append(list4[:k])
k_shot_new_train.append(list5[:k])
k_shot_new_train.append(list6[:k])
k_shot_new_train.append(list7[:k])
k_shot_new_train.append(list8[:k])
k_shot_new_train.append(list9[:k])
k_shot_new_train.append(list10[:k])
        
json_object = json.dumps(k_shot_new_train, indent = 4) 
  
# Writing to sample.json 
with open("10way_train_ft_10.json", "w") as outfile: 
    outfile.write(json_object) 

# ------------ pre-train -----------------
import json

with open('dev.json', 'r') as f:
    data = json.load(f)
    
new_test = []
    
event_type_list = []
for i in range(len(data)):
    sentence = data[i]
    
    if(sentence['golden-event-mentions']!=[]):
        event_type = sentence['golden-event-mentions'][0]['event_type']
        
        for j in train_event_type:
            if(event_type==j):
                new_test.append(sentence)
                continue
    
        event_type_list.append(event_type)

# Serializing json  
json_object = json.dumps(new_test, indent = 4) 
  
# Writing to sample.json 
with open("10way_dev_pre.json", "w") as outfile: 
    outfile.write(json_object) 

