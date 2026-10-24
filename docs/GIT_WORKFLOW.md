# Git & GitHub Workflow

## Initial setup
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Create a new empty GitHub repository named `Ecommerce-Sales-Data-Analytics`, then clone it:
```bash
git clone https://github.com/YOUR-USERNAME/Ecommerce-Sales-Data-Analytics.git
cd Ecommerce-Sales-Data-Analytics
```
Copy the project files into the cloned folder.

## Meaningful commits
Make commits at real milestones rather than one giant commit:
```bash
git add README.md requirements.txt .gitignore docs/
git commit -m "Add project documentation and repository structure"
git push -u origin main

git add data/ notebooks/ scripts/
git commit -m "Add dataset preparation and exploratory analysis"
git push

git add visualizations/ powerbi/
git commit -m "Add analysis charts and Power BI dashboard guide"
git push

git add report/ presentation/ screenshots/
git commit -m "Add final report and project presentation"
git push
```

Practice pull:
```bash
git pull origin main
```
Run `git status` before each commit. Do not commit credentials or private data. Replace `YOUR-USERNAME` with your own GitHub username.
