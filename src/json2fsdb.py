import json
import os
import uuid

with open("../data/comments_data.json",'r',encoding="utf-8") as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
# load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]

data_tree = {}
for it in load_dict:
	# 这里建立了一个嵌套的map结构 用来保存树型*目录结构*
	# 若没有就建立
	if not it['school_cate'] in data_tree:
		data_tree[it['school_cate']] = {}
		print('add school_cate: ' + it['school_cate'])
	if not it['university'] in data_tree[it['school_cate']]:
		data_tree[it['school_cate']][it['university']] = {}
		print('add ' + it['university'] + ' in ' + it['school_cate'])
	if not it['department'] in data_tree[it['school_cate']][it['university']]:
		data_tree[it['school_cate']][it['university']][it['department']] = [] # 对这个结构来说，supervisor是root
	if not it['supervisor'] in data_tree[it['school_cate']][it['university']][it['department']]:
		data_tree[it['school_cate']][it['university']][it['department']].append(it['supervisor'])

# 建立目录和索引
cate_map = {}
for cate in data_tree:
	cate_map[cate] = str(uuid.uuid4())
	os.makedirs(r'../fsdb/' + cate_map[cate])
	print(cate)
	univ_map = {}
	for univ in data_tree[cate]:
		univ_map[univ] = str(uuid.uuid4())
		os.makedirs(r'../fsdb/' + cate_map[cate] +'/'+ univ_map[univ])
		print('---'+univ)
		dep_map = {}
		for dep in data_tree[cate][univ]:
			dep_map[dep] = str(uuid.uuid4())
			os.makedirs(r'../fsdb/' + cate_map[cate] +'/'+ univ_map[univ] +'/'+ dep_map[dep])
			print('------'+dep)
			sup_map = {}
			for sup in data_tree[cate][univ][dep]:
				sup_map[sup] = str(uuid.uuid4())
				os.makedirs(r'../fsdb/' + cate_map[cate] +'/'+ univ_map[univ] +'/'+ dep_map[dep] +'/'+ sup_map[sup])
				print('---------'+sup)
			with open("../fsdb/" + cate_map[cate] +'/'+ univ_map[univ]+'/'+ dep_map[dep] +'/'+ "sup_map.json","w") as dump_f:
				json.dump(sup_map,dump_f)
		with open("../fsdb/" + cate_map[cate]  +'/'+ univ_map[univ] +'/'+ "dep_map.json","w") as dump_f:
			json.dump(dep_map,dump_f)
	with open("../fsdb/"+cate_map[cate] +'/'+ "univ_map.json","w") as dump_f:
		json.dump(univ_map,dump_f)
with open("../fsdb/cate_map.json","w") as dump_f:
   	json.dump(cate_map,dump_f)
