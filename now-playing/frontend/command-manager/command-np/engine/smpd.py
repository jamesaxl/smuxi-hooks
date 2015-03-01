#-*- coding: utf-8 -*-
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# Version 2, December 2004
#
# Copyright (c) 2015 James Axl <axlrose112@gmail.com>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.

try:
    import mpd
except ImportError:
    print (u"ProtocolManager.Command /echo you need to install python-mpd :)")
    sys.exit()

class Mpd(object):

    def __init__(self):
        self.__client = mpd.MPDClient()
        try:
            self.__client.connect('localhost', '6600')
        except socket.error:
            print (u"ProtocolManager.Command /echo check you MPD connection :)")
            sys.exit()

    @classmethod
    def GetTrackInfos(cls):
        smpd = Mpd()
        output = smpd.__client.currentsong()['artist'] + ' - '+ smpd.__client.currentsong()['title']
        print(u"ProtocolManager.Command /me is playing: {}".format(output).encode("utf-8"))
        smpd.__client.close()
        smpd.__client.disconnect()
        sys.exit()
