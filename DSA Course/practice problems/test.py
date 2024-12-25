tasks_list=["Study","Revision","New learn","Meditation","Health","Exercise","Work","Time Waste","Anger","Maas","Hazard"]
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


score=[]

print("\n--Choose Yes|No--\n")

for i in range(len(tasks_list)):
    while True:
        try:
            ask=input(f"Choose for |{tasks_list[i]}|- ").strip().lower()
            if ask=="yes":
                score.append(yes_no_score[tasks_list[i]]["Yes"])
                break
            elif ask=="no":
                score.append(yes_no_score[tasks_list[i]]["No"])
                break
            else:
                raise ValueError("Option choosed is Invalid.")
        except ValueError:
            print("Wrong Option.\n--Choose Yes|No--\n")

print(score)