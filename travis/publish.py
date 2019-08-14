import os

os.chdir('/tmp')
os.system('git clone https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} pdfs 2>&1')
os.chdir('pdfs/')

pasteInfoLines = open("$TRAVIS_BUILD_DIR/pasteInfo.txt", "r").readlines()

i = 0
while i < len(pasteInfoLines):
  dir = pasteInfoLines[i]
  if (i + 1 >= len(pasteInfoLines)):
    break
  fileName = pasteInfoLines[i + 1]
  os.system("mkdir -p " + dir)
  os.system("cp $TRAVIS_BUILD_DIR/" + fileName + " " + dir + "/")
  i += 2


os.system('git config --global user.name $GIT_AUTHOR_NAME')
os.system('git config --global user.email $GIT_AUTHOR_EMAIL')
os.system('git config --global push.default matching')

os.system('git add -A')
os.system('git commit -m \"Adding latest build of pdf to pdfs repo\"')
os.system('git push https://${GH_OAUTH_TOKEN}@github.com/${GH_USER_NAME}/${GH_PROJECT_NAME} 2>&1')