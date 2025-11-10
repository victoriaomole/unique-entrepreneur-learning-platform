import os
import shutil

BASE_DIR = r"C:\Users\victo\kickoff_project"
TEMPLATE_NAME = "UniqueEntrepreneur_Discovery_Interview_Template.docx"

template_path = os.path.join(BASE_DIR, TEMPLATE_NAME)
target_dir = os.path.join(
    BASE_DIR,
    "01_Phase1_Discovery_and_Scoping",
    "Stakeholder_Interview_Notes"
)

if not os.path.exists(template_path):
    raise FileNotFoundError(
        f"Template not found at {template_path}. "
        f"Run generate_discovery_template.py first."
    )

os.makedirs(target_dir, exist_ok=True)

files_to_create = [
    "OrgAdmin_Interview_01.docx",
    "Instructor_Interview_02.docx",
    "Student_Interview_03.docx",
    "DMP_Compliance_Interview_04.docx",
    "ExecSponsor_Interview_05.docx",
    "TechLead_Interview_06.docx",
]

for fname in files_to_create:
    dest = os.path.join(target_dir, fname)
    shutil.copyfile(template_path, dest)

print("✅ Created stakeholder interview files in:")
print(target_dir)

