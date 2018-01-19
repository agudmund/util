#!/usr/bin/env python

from SysTrayIcon import SysTrayIcon
from pytube import YouTube
from tubetest import Fetch

this = Fetch()
this.refresh_history()

def list_menu_options(SysTrayIcon):
    print '--[ Main Options'

    count = 0
    for n in SysTrayIcon.menu_options:
        print '[%s] %s ID:%s' % (count,n[0],n[3])
        count = count+1
    print '> Please select Category'
    category = raw_input()

    count = 0

    for n in SysTrayIcon.menu_options[int(category)]:
        if type(n) == list:
            for y in n:
                print '[%s] %s ID: %s'%(count,y[0],y[3])
                count = count+1
    print '> Please select Subcategory'
    subcat = raw_input()
    content = SysTrayIcon.menu_options[int(category)][2][int(subcat)][2]
    for n in content:
        print n[0],n[3]
        

def last_ten(SysTrayIcon):
    history = [n for n in SysTrayIcon.menu_options[0][2][2][2]]

    video = [n for n in history if n[3] == SysTrayIcon.id_execute]
    target = [n for n in this.youtube_history if n[2] == video[0][0]]
    url = target[0][1]
    this.grab(url)

def all_history(SysTrayIcon):

    history = [n for n in SysTrayIcon.menu_options[0][2][1][2]]

    video = [n for n in history if n[3] == SysTrayIcon.id_execute]
    target = [n for n in this.youtube_history if n[2] == video[0][0]]
    url = target[0][1]
    this.grab(url)

def exit(sysTrayIcon):
    print 'App exit.  See you next time.'

def RefreshHistory(sysTrayIcon):
    this.refresh_history()
    sysTrayIcon.refresh_icon()
    return True

menu_options =  (
    ('YouTube', None,   [
        ('Refresh History',None,RefreshHistory),
        ('All History', None, ( [(n[2],None,all_history) for n in this.youtube_history] ) ),
        ('Last Ten', None, ( [(n[2],None,last_ten) for n in this.youtube_history[-10:]] ) )
                        ]  ),
    ('Debug',None,(
        ('List menu Options',None,list_menu_options),('This',None,list_menu_options)

        ))


                )

SysTrayIcon('./Icons/Icon.ico','Utilitarian',menu_options,on_quit=exit, default_menu_index=1)