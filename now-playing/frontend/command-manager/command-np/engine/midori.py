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

import bernami
import sys

class Midori(bernami.Bernami):

    @classmethod
    def MidoriTrackInfos(cls):
        super(Midori, cls).MidoriTrackInfos()
        if cls._iface:
            properties = cls._iface.GetAll('org.midori.mediaHerald')
            output = properties.get("VideoTitle")[1:] + ' - '+ properties.get("VideoUri")[0:]
            print(u"ProtocolManager.Command /me is playing: {}".format(output).encode("utf-8"))
            sys.exit()
