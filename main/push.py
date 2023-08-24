from os import system
system('del db.sqlite3')
system('git add .')
system(f'git commit -m "{system("whoami")}')
system('git push https://github.com/codesniper3301-coders/heist_3301.git')
print('Done')