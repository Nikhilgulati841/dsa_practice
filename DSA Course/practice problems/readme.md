STEP 1: Install Prerequisites on Your Machine
Install Python (Ensure Python 3.7 or later is installed).

Install Kivy:
Run the following command:

pip install kivy
Install Buildozer:
Buildozer is essential for packaging your .apk file. Install it via pip:

pip install buildozer
Install Build Tools (Linux only):
If you're using Linux, you need additional tools:

sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip python3-venv
For Windows/Mac users:
Use WSL (for Windows) or set up a VM with Ubuntu Linux to use Buildozer, as it's primarily built for Linux.

STEP 2: Modify Your Python Code to Work with Kivy
Kivy is primarily used for GUI-based applications. Since your code is CLI (text-based), you'll need a simple GUI interface or just run it as-is.

Below is the adjusted Python code with a minimal Kivy GUI:

main.py
```
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def calculate_score(task_list, yes_no_score):
    score = []
    for i in task_list:
        ask = input(f"Done with |{i}| (yes/no): ").strip().lower()
        if ask in ["yes", "no"]:
            score.append(yes_no_score[i][ask.capitalize()])
        else:
            score.append(0)  # Default if input is invalid
    return score


def calculate_weightage(task_list, yes_no_score, score):
    negative_list = []
    for i in task_list:
        if i in ["Time Waste", "Anger", "Maas", "Hazard"]:
            negative_list.append(yes_no_score[i]["Yes"])
        else:
            negative_list.append(yes_no_score[i]["No"])

    positive_list = []
    for i in task_list:
        if i in ["Time Waste", "Anger", "Maas", "Hazard"]:
            positive_list.append(yes_no_score[i]["No"])
        else:
            positive_list.append(yes_no_score[i]["Yes"])

    weightage = []
    n = len(task_list)
    for i in range(0, n):
        positive = yes_no_score[task_list[i]]["Yes"]
        negative = yes_no_score[task_list[i]]["No"]

        if score[i] > 0:
            weightage.append(round(score[i] * (100 / sum(positive_list)), 2))

        elif score[i] <= 0:
            total_part_points = abs(negative) + abs(positive)
            weightage.append(round(total_part_points * (100 / sum(positive_list)), 2))

    return weightage, positive_list, negative_list


def bubble_sort_weightage(weightage, task_list, score):
    n = len(task_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if weightage[j] < weightage[j + 1]:
                weightage[j], weightage[j + 1] = weightage[j + 1], weightage[j]
                task_list[j], task_list[j + 1] = task_list[j + 1], task_list[j]
                score[j], score[j + 1] = score[j + 1], score[j]
    return weightage, task_list, score


def display_results(weightage, task_list, score, positive_list, negative_list, yes_no_score):
    result = "\nYour Score: {}\n".format(sum(score))
    result += f"Maximum Positive Score: {sum(positive_list)}\n"
    result += f"Maximum Negative Score: {sum(negative_list)}\n"
    for i in range(len(task_list)):
        result += f"{task_list[i]}: weight {weightage[i]}, score {score[i]}\n"
    return result


class MainApp(App):
    def build(self):
        self.task_list = [
            "Study",
            "Revision",
            "New learn",
            "Meditation",
            "Health",
            "Exercise",
            "Work",
            "Time Waste",
            "Anger",
            "Maas",
            "Hazard",
        ]

        self.yes_no_score = {
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

        self.root = BoxLayout(orientation="vertical")
        self.result_label = Label(text="Enter input:")
        self.start_button = Button(text="Run Program")
        self.start_button.bind(on_press=self.run_program)

        self.root.add_widget(self.result_label)
        self.root.add_widget(self.start_button)
        return self.root

    def run_program(self, instance):
        score = calculate_score(self.task_list, self.yes_no_score)
        weightage, positive_list, negative_list = calculate_weightage(
            self.task_list, self.yes_no_score, score
        )
        weightage, task_list, score = bubble_sort_weightage(
            weightage, self.task_list, score
        )
        result = display_results(
            weightage, self.task_list, score, positive_list, negative_list, self.yes_no_score
        )
        self.result_label.text = result


if __name__ == "__main__":
    MainApp().run()
```
STEP 3: Set Up Buildozer
Create a new directory and place your main.py there.
Run the following command to initialize Buildozer:
buildozer init
This will generate a buildozer.spec file. Open it and modify key settings as follows:
[app]
title = YourAppName
package.name = yourappname
package.domain = org.yourdomain
source.dir = .
source.exclude_exts = pyc
requirements = python3,kivy
orientation = portrait
fullscreen = 1
STEP 4: Build the APK
Run the following command to build the APK:

buildozer -v android debug
This process will take time as Buildozer downloads and compiles necessary dependencies.

STEP 5: Transfer and Install APK
Once the APK is built, it will be located in the bin/ folder of your project directory.
Transfer the APK to your Android device using a USB cable or upload it to cloud storage (e.g., Google Drive).
Install the APK on your Android device.
