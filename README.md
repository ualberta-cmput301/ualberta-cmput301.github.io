# ualberta-cmput301.github.io <!-- @LT-IGNORE:GITHUB@ -->
CMPUT 301 Website

<https://ualberta-cmput301.github.io/>

Please file an issue if you find anything wrong or missing on the site.

# Installation

- Clone the repository (**git clone https://github.com/ualberta-cmput301/ualberta-cmput301.github.io.git**)

- Change directory (**cd ualberta-cmput301.github.io**)

- Create a virtual environment (**virtualenv venv --python=python3**)

- Activate the virtual environment (Mac **source venv/bin/activate** Windows **venv/bin/activate**)

- Install requirements (**pip install -r requirements.txt**)

# Running 


- Test locally (**make devserver**)

- Deploy live (**make github**)

# N.B Please ensure you make changes on a seperate branch, test it locally before deploying to main branch

# Dev Notes

- Do not modify the themes, static files (like exercises) go into
  static folders.
  
- Do not link to google docs or google drive or google forms, link to
  canvas. We get too much spam when people don't use the UA
  credentials.
  
- Use `{filename}` for static content to avoid these warnings:
```
           WARNING  {filename} used for linking to static content /resources/practice/PracticeQuestions.pdf in general/midterms.md. Use {static} instead                                                                                contents.py:319
```

# Per Term Migration

- Each term grep for canvas URLs and update them like: `./content/projects/project_part1.md`
