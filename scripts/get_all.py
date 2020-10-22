from util import *
import os
import json

pages=os.listdir('pages')
all_linkes=[]
for page in pages:
    if 'page' not in page:continue
    path='pages/'+page
    src=open(path,'r',encoding='utf-8').read()
    links=getLinkes(src)
    all_linkes+=links


else:save('recipe_linkes.json',json.dumps(all_linkes))
print('done')
