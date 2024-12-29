def calculate_score(task_list,yes_no_score):
    score=[]
    print("\nChoose Yes | No\n")
    for i in task_list:
        while True:
            try:
                ask=input(f"Done with |{i}|- ").strip().lower()
                if ask in ["yes","no"]:
                    score.append(yes_no_score[i][ask.capitalize()])
                    break
                else:
                    raise ValueError("Invalid option.")
            except ValueError:
                print("Wrong Option.\nChoose Yes | No\n")
    return score

def calculate_weightage(task_list,yes_no_score,score):
    negative_list=[]
    for i in task_list:
        # if i=="Time Waste" or "Anger" or "Maas" or "Hazard":  in this method, python finds all anger, maas etc as String and non-empty strings are considered as True in boolean context, so this will always print as if i=="Time Waste" or True:
        if i in ["Time Waste","Anger","Maas","Hazard"]:
            negative_list.append(yes_no_score[i]["Yes"])
        else: 
            negative_list.append(yes_no_score[i]["No"])
        
    positive_list=[]
    for i in task_list:
        if i in ["Time Waste","Anger","Maas","Hazard"]:
            positive_list.append(yes_no_score[i]["No"])
        else:
            positive_list.append(yes_no_score[i]["Yes"])
        
    weightage=[]
    n=len(task_list)
    for i in range(0,n):
        positive=yes_no_score[task_list[i]]["Yes"]
        negative=yes_no_score[task_list[i]]["No"]
     
        if score[i]>0:
            weightage.append(round(score[i]*(100/sum(positive_list)),2))
            
        elif score[i]<=0:
            total_part_points=abs(negative)+abs(positive)
            weightage.append(round(total_part_points*(100/sum(positive_list)),2))
            
            
    return weightage, positive_list, negative_list
    
def bubble_sort_weightage(weightage,task_list,score):
    n=len(task_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if weightage[j]<weightage[j+1]:
                weightage[j], weightage[j+1]=weightage[j+1], weightage[j]
                task_list[j], task_list[j+1]=task_list[j+1], task_list[j]
                score[j], score[j+1]=score[j+1], score[j]
            
    return weightage, task_list, score
    
def display_results(weightage,task_list,score,positive_list,negative_list,yes_no_score):
    print(f"\nYour Score: {sum(score)}\n")
    print(f"""\n----------------------------
Maximum Positive Score: {sum(positive_list)}
Maximum Negative Score: {sum(negative_list)}
----------------------------\n""")
    print("--From the most weightated task to the lowest weightated--\n")
  
    for i in range(len(task_list)):
        if score[i]>0:
            print(f"|| Your choosen option gives {task_list[i]}'s Score: {score[i]} ||| Which Impacts your Today's by {weightage[i]}% ||| ")
        else:
            positive=yes_no_score[task_list[i]]["Yes"]
            negative=yes_no_score[task_list[i]]["No"]
            if task_list[i] in ["Time Waste","Anger","Maas","Hazard"]:
                print(f"|| Your choosen option gives {task_list[i]}'s Score: {score[i]} ||| Which Impacts your Today's score by {weightage[i]}% |||\nAs here ==> Score is subtracted by {score[i]} and Positive part|{negative}| also does not adds up to Today's score\n")
            
            else:
                print(f"|| Your choosen option gives {task_list[i]}'s Score: {score[i]} ||| Which Impacts the score by {weightage[i]}% |||\nAs here ==> Score is subtracted by {score[i]} and Positive part|{positive}| also does not adds up to Today's score\n")
            
    print(f"\nTotal Weightage: {sum(weightage)}")

def main():
    task_list=["Study","Revision","New learn","Meditation","Health","Exercise","Work","Time Waste","Anger","Maas","Hazard"]

    yes_no_score={"Study":{"Yes":22,"No":-25},
              "Revision":{"Yes":10,"No":-8},
              "New learn":{"Yes":7,"No":0},
              "Meditation":{"Yes":7,"No":-8},
              "Health":{"Yes":8,"No":-12},
              "Exercise":{"Yes":8,"No":-9},
              "Work":{"Yes":7,"No":-8},
              "Time Waste":{"No":10,"Yes":-25},
              "Anger":{"No":10,"Yes":-15},
              "Maas":{"No":10,"Yes":-7},
              "Hazard":{"No":8,"Yes":-10}}
    # score=calculate_score(task_list,yes_no_score)
    score=calculate_score(task_list,yes_no_score)
    weightage, positive_list, negative_list=calculate_weightage(task_list,yes_no_score,score)
    
    weightage, task_list, score=bubble_sort_weightage(weightage,task_list,score)
    
    display_results(weightage,task_list,score,positive_list,negative_list,yes_no_score)

main()
    
