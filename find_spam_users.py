import json
import urllib2

def get_feed():
    fd = urllib2.urlopen(
        'http://forum.openhatch.org/discussions.json')
    s = fd.read()
    return json.loads(s)

def prompt_for_spammy_content(spam_author_ids,
                              iterable_of_discussions):
    for discussion in iterable_of_discussions:
        author_id = int(discussion['FirstUserID'])
        if author_id in spam_author_ids:
            continue # next discussion

        body = discussion['Body']
        print body

        print "Is this spam?"
        yes_no = raw_input("y/N >")[:1].lower()
        if yes_no == 'y':
            spam_author_ids.add(author_id)

def in_feed_look_for_spammy_users(feed):
    spam_authors = set()

    if hasattr(feed['Discussions'], 'values'):
        discussions = feed['Discussions'].values()
    else:
        discussions = feed['Discussions']

    discussions_reformatted = [
        value for value in discussions
        if value]

    for data_source in (
        feed['Announcements'],
        discussions_reformatted):
        prompt_for_spammy_content(spam_authors,
                                  data_source)

    return spam_authors

def make_deletion_urls(user_ids):
    for user_id in user_ids:
        print "http://forum.openhatch.org/user/delete/%d/delete" % (
            user_id,)
