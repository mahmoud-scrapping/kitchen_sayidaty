from util import *
import os

recipes=[]
pages=os.listdir('recipes')
bad=0
for i in range(len(pages)):
    page=pages[i]
    if i%100==0:print(i)
    path='recipes/'+page
    src=load(path,encode=True)
    recipe=getDetails(src)
    if recipe==None:
      bad+=1
      continue
    recipes.append(recipe)
else:save('recipes.json',recipes,encode=True,is_json=True)

print('done, good :',len(recipes),', bad :',bad)

