'''
Created on Oct 14, 2015

@author: Ryan
'''

import praw

user_agent = "Karma Breakdown 1.0 by /u/stirus"
r = praw.Reddit(user_agent=user_agent)

user_name = "stirus"
user = r.get_redditor(user_name)

thing_limit = 10
gen = user.get_submitted(limit = thing_limit)

karma_by_subreddit = {}

for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

import pprint
pprint.pprint(karma_by_subreddit)