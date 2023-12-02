import os
import shutil

for i in range(1, 25 + 1):
    day_dir = f"./Day {i}"
    if os.path.exists(day_dir):
        continue
        shutil.rmtree(day_dir)
    os.mkdir(day_dir)
    with open(f"{day_dir}/input.txt", "w") as f:
        f.write("")
        f.close()
    for part in range(1, 3):
        with open(f"{day_dir}/example{part}.txt", "w") as f:
            f.write("")
            f.close()
        with open(f"{day_dir}/solution_part{part}.py", "w") as f:
            f.write("")
            f.close()
        with open(f"{day_dir}/question_part{part}.md", "w") as f:
            f.write("")
            f.close()

print("DONE")
