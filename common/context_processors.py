# coding=utf-8
from common.models.friendlink import FriendLink

def friend_links(request):
    return {'friend_links': FriendLink.objects.all(),}
