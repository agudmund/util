
import os
import random
import json
#import shotgun_api3 as shotgun

import shotgun_api3

SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)

# data = {
#       'project': {"type":"Project","id": 89},
#       'code': num,
#       'description': '',
#       'sg_status_list': 'ip'
# }

#

def getProject(sg,project):
    # let's find the project
    filters = [
        ['name', 'is', project]
    ]
    fields = ['id', 'name']
    print sg.find_one('Project', filters, fields)

def find_asset_tasks(sg, project, asset):
    print "searching:", project, "for Asset called:", asset
    filters = [
        ['project.Project.name', 'is', project],
        ['entity.Asset.code', 'is', asset],
        ]
    fields = ['content', 'id','name']
    sg_tasks = sg.find("Task", filters, fields)
    # pprint(sg_tasks)
    return sg_tasks



filters = [
    ["sg_status_list", "is_not", "fin"],
    ["sg_status_list", "is_not", "hld"],
    {
        "filter_operator": "any",
        "filters": [
        ['project.Project.name', 'is', "Match Dot Com"]
            # ["assets", "is", {"type": "Asset", "id": 9}],
            # ["assets", "is", {"type": "Asset", "id": 23}]
        ]
    }
]

def pickOne():

    result = sg.find("Asset", filters,['content', 'id','project','code','type'])


    rez = random.choice(result)
    print 'Still stuff to do on', rez['code'], 'in', rez['type']

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


# thumbpath = os.getcwd()
# thumbs = [ n for n in os.listdir(thumbpath) if n.endswith('.jpg')]


# for i in thumbs:

#   print "Creating shot"
#   num = os.path.splitext(i)[0][-4:]

#   data = {
#       'project': {"type":"Project","id": 86},
#       'code': num,
#       'description': '',
#       'sg_status_list': 'ip'
# }

#   result = sg.create('Shot', data)
#   print result['id'],num

#   sg.upload_thumbnail('Shot', result['id'], os.path.join(thumbpath,i) )


