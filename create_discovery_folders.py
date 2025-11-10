import os

base = r"C:\Users\victo\kickoff_project"

folders = [
    "01_Phase1_Discovery_and_Scoping",
    "01_Phase1_Discovery_and_Scoping/Stakeholder_Interview_Notes",
    "01_Phase1_Discovery_and_Scoping/Personas_and_UserJourneys",
]

for folder in folders:
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)

print("✅ Folder structure created successfully under kickoff_project/")

