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
import subprocess
import getpass

USER = getpass.getuser()

try:
    import dbus
except ImportError:
    print (u"ProtocolManager.Command /echo you need to install python-dbus :)")
    sys.exit()

class Bernami(object):
    session_bus = dbus.SessionBus()
    
    def BernamiProc(self, deamon):
        try:
            player_pid = subprocess.check_output(['pgrep', deamon, '-u', USER])
            return player_pid
        except subprocess.CalledProcessError:
            return False

    @classmethod
    def MprisTrackInfos(cls, mplayer):
        cls.__bernamiproc = Bernami()
        if cls.__bernamiproc.BernamiProc(mplayer):
            cls._string = dbus.String
            player = Bernami.session_bus.get_object('org.mpris.MediaPlayer2.%s' %mplayer, '/org/mpris/MediaPlayer2')
            cls._iface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
        else:
            cls._iface = None

    @classmethod
    def MidoriTrackInfos(cls):
        cls.__bernamiproc = Bernami()
        if cls.__bernamiproc.BernamiProc('midori'):
            player = Bernami.session_bus.get_object('org.midori.mediaHerald','/org/midori/mediaHerald')
            cls._iface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
        else:
            cls._iface = None
