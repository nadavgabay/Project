__author__ = 'nadav'
# -*- coding: utf-8 -*-
import facebook
from Post import *
from EmailSender import *
import itertools

class facebookUtils:


    def __init__(self):
        self.listOfGroups=[]
        counter=0
        self.email = EmailSender("5492nadav@gmail.com")
        self.updatedUserListOfAllHisSearchPosts=[]
        self.listOfAllPosts=[]

    def setAccessToken(self,token):
        self.token = token
        self.graph = facebook.GraphAPI(self.token)
        group = self.graph.get_object("me")
        self.all_groups = self.graph.get_connections("me","groups")

    def getGroupsNames(self):
        while(self.all_groups['data']):
            try:
                for groupy in self.all_groups['data']:
                    if groupy['name'] in self.listOfGroups:
                        # import pdb;pdb.set_trace();
                        return self.listOfGroups
                    self.listOfGroups.append(groupy['name'])
            except KeyError:
               print "Key Error"


    def getGroupPosts(self,namesOfAllGroupsToSearchIn=[]):
        group_data=[]
        for currenctgroup in namesOfAllGroupsToSearchIn:
            group_data.append(self.searchInAllPosts(currenctgroup))
        return group_data

    def searchInAllPosts(self,currenctgroup):
        while(self.all_groups['data']):
                try:
                    for groupy in self.all_groups['data']:
                        if currenctgroup == groupy['name']:
                            group_id = groupy['id']
                            return self.graph.get_connections(group_id, "feed")['data']
                except KeyError:
                    print "Key Error"

    def parse_posts(self,allPosts, searchWithAndBetweenWords, words_to_saerch):
        localListOfPosts=[]
        tempList=""
        for posts in allPosts:
            for i in posts:
                if (i.get('message') is None) or (any(i.get('message') in pst.getMessage() for pst in self.listOfAllPosts)):
                    print i.get('message')
                    pass
                else:
                    #encodeString = i.get('message')
                    try:
                        encodeString = i.get('message').encode('utf8')
                    except:
                        encodeString = unicode(i.get('message')).encode('utf8')
                    if searchWithAndBetweenWords != 'on':
                        if any(word in encodeString for word in words_to_saerch):
                            post = Post(i.get('from').get('name'), i.get('message'), i.get('to').get('data')[0].get('name'), i.get('created_time'))
                            self.listOfAllPosts.append(post)
                            localListOfPosts.append(post)
                    else:  ## If set to ON
                        if all(word in encodeString for word in words_to_saerch):
                            post = Post(i.get('from').get('name'),i.get('message'),i.get('to').get('data')[0].get('name'),i.get('created_time'))
                            self.listOfAllPosts.append(post)
                            localListOfPosts.append(post)
        for item in itertools.chain(localListOfPosts):
            tempList += item.getMessage()
        if tempList != "":
            self.email.login(tempList.encode('utf8'))
        return self.listOfAllPosts
