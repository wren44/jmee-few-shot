#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:58:15 2020

@author: conniemessi
"""


# 'Convict' 'Marry' 'Elect' 'Start-Org' 'Start-Position'

import json

with open('train.json', 'r') as f:
    data = json.load(f)
    
base_event_type = ['Justice:Convict', 'Life:Marry', 'Personnel:Elect', 'Business:Start-Org', 'Personnel:Start-Position']

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
with open("dev_ft.json", "w") as outfile: 
    outfile.write(json_object) 



# ------ k shot train -------
with open('train.json', 'r') as f:
    data = json.load(f)
    
k_shot = 5

list1,list2,list3,list4,list5 = [],[],[],[],[]

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

k_shot_new_train = []           
k_shot_new_train.append(list1[:5])
k_shot_new_train.append(list2[:5])
k_shot_new_train.append(list3[:5])
k_shot_new_train.append(list4[:5])
k_shot_new_train.append(list5[:5])
        
json_object = json.dumps(k_shot_new_train, indent = 4) 
  
# Writing to sample.json 
with open("train_ft_5.json", "w") as outfile: 
    outfile.write(json_object) 

# ------------ pre-train -----------------
import json

with open('test.json', 'r') as f:
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
with open("test_pre.json", "w") as outfile: 
    outfile.write(json_object) 

