import os
import shutil

for i in range(1, 32):
    day_dir = f"./Day {i}"
    if os.path.exists(day_dir):
        break
        shutil.rmtree(day_dir)
    os.mkdir(day_dir)
    with open(f"{day_dir}/input.txt", "w") as f:
        f.write("")
        f.close()
    with open(f"{day_dir}/solution.py", "w") as f:
        f.write("")
        f.close()
    with open(f"{day_dir}/question.md", "w") as f:
        f.write("")
        f.close()

print("DONE")
