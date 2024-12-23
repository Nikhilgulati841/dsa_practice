def get_user_input(tasks_list, yes_no_score):
    """
    Get user input for each task and calculate the score based on the responses.
    """
    score = []
    print("\nChoose Yes | No\n")
    for task in tasks_list:
        ask = input(f"Done with |{task}| - ")
        if ask.lower() == "yes":
            score.append(yes_no_score[task]["Yes"])
        elif ask.lower() == "no":
            score.append(yes_no_score[task]["No"])
    return score


def calculate_weightage(tasks_list, yes_no_score):
    """
    Calculate weightage percentage for each task based on their positive and negative scores.
    """
    total_positive_negative = 0
    weightage = []

    # Step 1: Calculate total positive + negative weight
    for task in tasks_list:
        positive = yes_no_score[task]["Yes"]
        negative = yes_no_score[task]["No"]
        total_positive_negative += abs(positive) + abs(negative)

    # Step 2: Calculate individual weightage for each task
    for task in tasks_list:
        positive = yes_no_score[task]["Yes"]
        negative = yes_no_score[task]["No"]
        weightage.append(round((abs(positive) + abs(negative)) * (100 / total_positive_negative), 2))

    return weightage


def bubble_sort_by_weightage(tasks_list, weightage):
    """
    Perform bubble sort on weightage and tasks_list simultaneously.
    """
    n = len(weightage)
    for i in range(n):
        for j in range(0, n - i - 1):
            if weightage[j] < weightage[j + 1]:
                # Swap weightage
                weightage[j], weightage[j + 1] = weightage[j + 1], weightage[j]
                # Swap corresponding task
                tasks_list[j], tasks_list[j + 1] = tasks_list[j + 1], tasks_list[j]
    return tasks_list, weightage


def display_results(score, tasks_list, weightage):
    """
    Display the results including the user's total score, weightage breakdown, and sorted list.
    """
    print("""
----------------------------
Maximum Positive Score: 107
Maximum Negative Score: -127
----------------------------
""")
    print(f"Your Score: {sum(score)}\n")
    print("--The weightage for each Task--")
    for i in range(len(tasks_list)):
        print(f"Impacted Percentage of {tasks_list[i]}: {weightage[i]}%")


def main():
    yes_no_score = {
        "Study": {"Yes": 22, "No": -25},
        "Revision": {"Yes": 10, "No": -8},
        "New learn": {"Yes": 7, "No": 0},
        "Meditation": {"Yes": 7, "No": -8},
        "Health": {"Yes": 8, "No": -12},
        "Exercise": {"Yes": 8, "No": -9},
        "Work": {"Yes": 7, "No": -8},
        "Time Waste": {"No": 10, "Yes": -25},
        "Anger": {"No": 10, "Yes": -15},
        "Maas": {"No": 10, "Yes": -7},
        "Hazard": {"No": 8, "Yes": -10},
    }

    tasks_list = ["Study", "Revision", "New learn", "Meditation", "Health", "Exercise", "Work", 
                  "Time Waste", "Anger", "Maas", "Hazard"]

    # Step 1: Get user input and calculate scores
    score = get_user_input(tasks_list, yes_no_score)

    # Step 2: Calculate weightage
    weightage = calculate_weightage(tasks_list, yes_no_score)
    display_results(score, tasks_list, weightage)


    # Step 3: Bubble sort tasks by weightage
    tasks_list, weightage = bubble_sort_by_weightage(tasks_list, weightage)
    print("\nSorted List\n")

    # Step 4: Display results
    display_results(score, tasks_list, weightage)


if __name__ == "__main__":
    main()