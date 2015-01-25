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

import sys
import bernami
#BEFORE ADD ANY PLAYER TO 'MPLAS' TUPLE BE SURE PLEASE THAT IT SUPPORTS MPRIS2
MPLAS = ('vlc', 'rhythmbox', 'clementine', 
        'spotify', 'tomahawk', 'amarok', 
        'banshee')

class MprisPlayer(bernami.Bernami):

    @classmethod
    def MprisTrackInfos(cls):

        for mpla in MPLAS :
            super(MprisPlayer, cls).MprisTrackInfos(mpla)
            if cls._iface:
                player_stat = cls._iface.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
                if player_stat == 'Playing':
                    try:
                        artist = cls._iface.Get('org.mpris.MediaPlayer2.Player','Metadata').get(cls._string(u'xesam:artist'))[0]
                        if artist == None: artist = 'Unknown'
                    except TypeError:
                        artist = 'Unknown'

                    try:
                        title = cls._iface.Get('org.mpris.MediaPlayer2.Player','Metadata').get(cls._string(u'xesam:title'))
                        if title == None: title = 'Unknown'
                    except TypeError:
                        title = 'Unknown'

                    output = artist + ' - '+ title
                    print(u"ProtocolManager.Command /me is playing: {}".format(output).encode("utf-8"))
                    sys.exit()
