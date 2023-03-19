# coding=utf8

import os
import random
import string

def gen_random_code():
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(16)))
    return(str(result_str))

class Swedish:
    
    def __init__(self):
        
        self.swedish_file_header = "code,swedish,english,fail,pass,used\n"
        self.swedish_file_db = "swedish.csv"
        self.swedish_progress = "progress.csv"
        self.swedish_data = None
        self.swedish_dicts_size = 0
        self.swedish_dicts = []
        self.swedish_five = []
        
    def init_console(self):
        
        os.system('prompt $')
        os.system('color 0c')
        os.system('title Swedish Language Learn')
        os.system('cls')
        
    def add_new_words(self):
        
        swedish_data = []
        
        with open(self.swedish_file_db) as j:
            content = j.readlines()

        data = [x.strip() for x in content];
        
        for line in data:
            
            if line != "swedish,english,fail,pass,used":
                
                line_split = line.split(",")
                
                d_swe = line_split[0]
                d_eng = line_split[1]
                d_fail = int(line_split[2])
                d_pass = int(line_split[3])
                d_used = int(line_split[4])

                swedish_data.append({"swedish":d_swe,"english":d_eng,"fail":d_fail,"pass":d_pass,"used":d_used})      
                
        added = 0

        for sload in swedish_data:
            
            found = 0
            
            d_swe = sload["swedish"]
            d_eng = sload["english"]
            d_fail = 0
            d_pass = 0
            d_used = 0           
        
            for item in self.swedish_dicts:
                if sload["swedish"] in item['swedish']:
                    found = 1
                    break                
                
            if found == 0:
                added += 1
                print("adding new word:",sload["swedish"])
                self.swedish_dicts.append({"code":gen_random_code(),"swedish":d_swe,"english":d_eng,"fail":d_fail,"pass":d_pass,"used":d_used})
                
        if added == 0:
            print("no new words added")
        
    def load_data(self):
        
        if os.path.exists(self.swedish_progress):
            
            with open(self.swedish_progress) as j:
                content = j.readlines()
                
            self.swedish_data = [x.strip() for x in content];
            
            for line in self.swedish_data:
                
                if line != "code,swedish,english,fail,pass,used":
                    
                    line_split = line.split(",")
                    
                    d_swe = line_split[1]
                    d_eng = line_split[2]
                    d_fail = int(line_split[3])
                    d_pass = int(line_split[4])
                    d_used = int(line_split[5])
    
                    self.swedish_dicts.append({"code":gen_random_code(),"swedish":d_swe,"english":d_eng,"fail":d_fail,"pass":d_pass,"used":d_used})
                    
            print("loaded progress",len(self.swedish_dicts),"word pairs")
            
        else:                
    
            with open(self.swedish_file_db) as j:
                content = j.readlines()
                
            self.swedish_data = [x.strip() for x in content];
            
            for line in self.swedish_data:
                
                if line != "swedish,english,fail,pass,used":
                    
                    line_split = line.split(",")
                    
                    d_swe = line_split[0]
                    d_eng = line_split[1]
                    d_fail = int(line_split[2])
                    d_pass = int(line_split[3])
                    d_used = int(line_split[4])
    
                    self.swedish_dicts.append({"code":gen_random_code(),"swedish":d_swe,"english":d_eng,"fail":d_fail,"pass":d_pass,"used":d_used})
                
            print("loaded standard",len(self.swedish_dicts),"word pairs")
                
    def save_progress(self):
        with open (self.swedish_progress, "w") as sFile:
            sFile.write(self.swedish_file_header)    
            
        with open (self.swedish_progress, "a") as sFile:
            for line in self.swedish_dicts:
                
                d_c = str(line['code'])
                d_s = str(line['swedish'])
                d_e = str(line['english'])
                d_f = str(line['fail'])
                d_p = str(line['pass'])
                d_u = "0"

                sFile.write(d_c+","+d_s+","+d_e+","+d_f+","+d_p+","+d_u+"\n")
                
    def get_dict_size(self):
        self.swedish_dicts_size = len(self.swedish_dicts)
        
    def populate_five_pairs(self):
        for i in range(0,5):
            self.swedish_five.append(self.get_random())
            
    def update_pair_data(self,code,pair_data):
        counter = 0
        for pair in self.swedish_dicts:
            if pair['code'] == code:
                self.swedish_dicts[counter] = pair_data
            counter += 1

    def get_random(self):
        
        found = 0
        
        choice = None

        while found != 1:
            
            choice = random.choice(self.swedish_dicts)
            
            chooser = random.randint(1, 3)
            
            if chooser == 1:
            
                if int(choice["used"]) == 0 and int(choice["pass"]) < 2:
    
                    choice["used"] = 1
                    
                    code = choice["code"]
                    
                    counter = 0
                    for pair in self.swedish_dicts:
                        if pair['code'] == code:
                            self.swedish_dicts[counter] = choice
                        counter += 1                
    
                    found = 1
                    
                    return(choice)
                
            if chooser > 1:
           
               if int(choice["used"]) == 0 and int(choice["fail"]) >= 1:
   
                   choice["used"] = 1
                   
                   code = choice["code"]
                   
                   counter = 0
                   for pair in self.swedish_dicts:
                       if pair['code'] == code:
                           self.swedish_dicts[counter] = choice
                       counter += 1                
   
                   found = 1
                   
                   return(choice)         

    def get_five_pairs(self):
        self.swedish_five = []
        self.populate_five_pairs()

        return self.swedish_five

    def get_data(self):
        return self.swedish_dictspainter

learn = Swedish()
learn.load_data()
learn.add_new_words()
learn.init_console()

response = None

stage = 1

while response != "exit()":
    
    pairs = learn.get_five_pairs()
    
    proceed = 1
    
    if response == "exit()":
        break    
    
    while proceed == 1:
        
        score = 0
        
        if response == "exit()":
            break        

        for pair_data in pairs:
            
            choose_side = random.randint(1, 2)
            
            get_SWE = pair_data["swedish"]
            get_ENG = pair_data["english"]
            get_code = pair_data["code"]
            
            if choose_side == 1 : response = input("<<< SWE "+get_SWE+" >>> ")
            if choose_side == 2 : response = input("<<< ENG "+get_ENG+" >>> ")
            
            if response == "":
                response = "12345"
            
            if response == "exit()":
                break
            
            if choose_side == 1 :
                
                if "/" in get_ENG:
                    
                    if response in get_ENG:
                        pair_data["pass"] += 1
                        score = score + 1
                        learn.update_pair_data(get_code,pair_data)
                        print("correct!")
                    else:
                        pair_data["fail"] += 1
                        print("wrong!")
                        print("--------------->",get_ENG)
                else:
                    if response == get_ENG:
                        pair_data["pass"] += 1
                        score = score + 1
                        learn.update_pair_data(get_code,pair_data)
                        print("correct!")
                    else:
                        pair_data["fail"] += 1
                        print("wrong!")
                        print("--------------->",get_ENG)                    
                    
            if choose_side == 2 :
                
                if "/" in get_SWE:                
            
                    if response in get_SWE:
                        pair_data["pass"] += 1
                        score = score + 1
                        learn.update_pair_data(get_code,pair_data)
                        print("correct!")
                    else:
                        pair_data["fail"] += 1
                        print("wrong!")
                        print("--------------->",get_SWE)   
                else:
                    if response == get_SWE:
                        pair_data["pass"] += 1
                        score = score + 1
                        learn.update_pair_data(get_code,pair_data)
                        print("correct!")
                    else:
                        pair_data["fail"] += 1
                        print("wrong!")
                        print("--------------->",get_SWE)                       
                    
            if score == 5:
                proceed = 0
                stage += 1
                print("======next stage======")

        learn.save_progress()