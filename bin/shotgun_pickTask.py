#!/usr/bin/env C:/Python27/python.exe

import os
import sys
import random
import json

import shotgun_api3

SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)
proj = sys.argv[-1]


def listProjects():
	x=sg.find('Project',[],['name'])
	for n in x:
		print(n)

def getProject(sg,project):
    filters = [['name', 'is', project]]
    fields = ['id', 'name']
    print (sg.find_one('Project', filters, fields))

def find_asset_tasks(sg, project, asset):
    print ("searching:", project, "for Asset called:", asset)
    filters = [
        ['project.Project.name', 'is', project],
        ['entity.Asset.code', 'is', asset],
        ]
    fields = ['content', 'id','name']
    sg_tasks = sg.find("Task", filters, fields)

    return sg_tasks

def pickOne():

    filters = [
    ["sg_status_list", "is_not", "fin"],
    ["sg_status_list", "is_not", "hld"],
    ["sg_status_list", "is_not", "omt"],
    {"filter_operator": "any",
        "filters": [
        ['project.Project.name', 'is', proj]
        ]}]
    result = sg.find("Asset", filters,['content', 'id','project','code','type'])

    rez = random.choice(result)
    print ('Still stuff to do on', rez['code'], 'in', rez['type'])

def uploadThumbnails():

    filters = [
    ["sg_status_list", "is_not", "fin"],
    ["sg_status_list", "is_not", "hld"],
    ["sg_status_list", "is_not", "omt"],
    {"filter_operator": "any",
        "filters": [
        ['project.Project.name', 'is', proj]
        ]}]

    result = sg.find("Asset", filters,['content', 'id','project','code','type'])

    rez = random.choice(result)
    thumbpath = r'C:\Users\normal\Projects\Match Dot Com\Documents'
    thumbs = [ os.path.join(thumbpath,n ) for n in os.listdir(thumbpath) if n.endswith(".JPG")]

    for asset in result:
        for thumb in thumbs:

            if asset['code'] == thumb.split('\\')[-1].split('.')[0]:
                print ('x',asset)
                sg.upload_thumbnail('Asset',asset['id'] , thumb ) # Needs python 3 apparently
                continue

if __name__ == '__main__':
    pickOne()
    

# for asset in result:
    # print find_asset_tasks(sg, "Match Dot Com", asset['code'])
# print find_asset_tasks(sg, "Match Dot Com", 1344)
# getProject(sg,"Match Dot Com")


# sg.summarize(entity_type='Task',
#               filters = [
#                  ['entity.Asset.sg_sequence', 'is', {'type': 'Sequence', 'id': 2}],
#                  ['sg_status_list', 'is_not', 'na']],
#               summary_fields=[{'field': 'id', 'type': 'count'}, {'field': 'due_date', 'type': 'latest'}],
#               grouping=[{'field': 'entity', 'type': 'exact', 'direction': 'asc'}])


# filters = [['id', 'is', 89]]
# result = sg.find_one('Project', filters)
# print (result)