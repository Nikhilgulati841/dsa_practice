def main():
    global tasks_list
    global yes_no_score
    # yes_dict={"Study":22,"Revision":10,"New learn":7,"Meditation":7,"Health":8,"Exercise":8,"Work":7,"Time Waste":10,"Anger":10,"Maas":10,"Hazard":8}
    # no_dict={"Study":-25,"Revision":-8,"New learn":0,"Meditation":-8,"Health":-12,"Exercise":-9,"Work":-8,"Time Waste":-25,"Anger":-15,"Maas":-7,"Hazard":-10}

tasks_list=["Study","Revision","New learn","Meditation","Health","Exercise","Work","Time Waste","Anger","Maas","Hazard"]
yes_no_score={"Study":{"Yes":22,"No":-25},"Revision":{"Yes":10,"No":-8},"New learn":{"Yes":7,"No":0},"Meditation":{"Yes":7,"No":-8},"Health":{"Yes":8,"No":-12},"Exercise":{"Yes":8,"No":-9},
                "Work":{"Yes":7,"No":-8},"Time Waste":{"No":10,"Yes":-25},"Anger":{"No":10,"Yes":-15},"Maas":{"No":10,"Yes":-7},"Hazard":{"No":8,"Yes":-10}}

score=[]
weightage={}

print("\nChoose Yes | No\n")
for i in range(len(tasks_list)):
    ask=input(f"Enter for {tasks_list[i]}: ")
    if ask.lower()=="yes":
        score.append(yes_no_score[tasks_list[i]]["Yes"])
        
    elif ask.lower()=="no":
        score.append(yes_no_score[tasks_list[i]]["No"])
    

print("""\n----------------------------
Maximum Positive Score: 107
Maximum Negative Score: -127
----------------------------\n""")

print(f"Your Score: {sum(score)}\n")
print("--The weightage for each Task--\n")

for i in range(len(score)):
    if score[i]<0:
        


