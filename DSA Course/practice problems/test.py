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
    negative_total=0
    for i in task_list:
        # if i=="Time Waste" or "Anger" or "Maas" or "Hazard":  in this method, python finds all anger, maas etc as String and non-empty strings are considered as True in boolean context, so this will always print as if i=="Time Waste" or True:


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
    print("\n",sum(score))

main()
    



