# Advent Of Code Repository Templates/Solutions

Generate template for you with questions in a markdown

# How To Use
1. Clone the repository
```bash
git clone https://github.com/UltraRaptorYT/AOC2023.git
```

2. Git checkout `template`
```bash
git checkout template
```

3. Initial the folder structure
```
AOC2023/
├── .env
├── .env.sample
├── .gitattributes
├── .gitignore
├── generateFolderStructure.py
├── getQuestion.py
├── README.md
└── requirements.txt
```

4. Add AOC_SESSION in`.env` file
    1. Login to <https://adventofcode.com/2023/day/2>
    2. Inspect Element [Press F12 or Right-Click `Inspect`]
    3. Click on `Application`
    4. Select `Cookies`
    5. Copy value from key `session`
    6. Paste value into `.env`

5. Install all the dependences
```bash
pip install -r requirements.txt
```

6. Run `generateFolderStructure.py`

Windows
```bash
python generateFolderStructure.py
```
MAC OS / LINUX
```bash
python3 generateFolderStructure.py
```

7. Run `getQuestion.py`

Windows
```bash
python getQuestion.py
```
MAC OS / LINUX
```bash
python3 getQuestion.py
```

**HAVE FUN SOLVING!!**

Final Tree Folder
```
AOC2023/
├── .env
├── .env.sample
├── .gitattributes
├── .gitignore
├── generateFolderStructure.py
├── getQuestion.py
├── README.md
├── requirements.txt
├── Day 1/
│   ├── input.txt
│   ├── example.txt
│   ├── example2.txt
│   ├── question_part1.md
│   ├── question_part2.md
│   └── solution_part1.py
│   └── solution_part2.py
├── Day 2/
│   ├── input.txt
│   ├── example.txt
│   ├── example2.txt
│   ├── question_part1.md
│   ├── question_part2.md
│   └── solution_part1.py
│   └── solution_part2.py
├── .
├── .
├── .
└── Day 25/
│   ├── input.txt
│   ├── example.txt
│   ├── example2.txt
│   ├── question_part1.md
│   ├── question_part2.md
│   └── solution_part1.py
│   └── solution_part2.py
```
