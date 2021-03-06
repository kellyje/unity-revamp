#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Authors:
#   J Phani Mahesh <phanimahesh@gmail.com>
#   Barneedhar (jokerdino) <barneedhar@ubuntu.com>
#   Amith KK <amithkumaran@gmail.com>
#
# Description:
#   Unit tests for unity reset.

import unittest
import unityreset

Gio=unityreset.Gio

class TestUnityReset(unittest.TestCase):
    '''Unittest for unity --reset'''
    def setUp(self):
        # Get defaults
        self.compizPlugins=unityreset.UnityReset.snapshotCompizPlugins()
        self.compizChildren=unityreset.UnityReset.snapshotCompizChildren()
        self.unityChildren=unityreset.UnityReset.snapshotUnityChildren()
    
    def test_show_hud(self):
        schema="org.compiz.integrated"
        key="show-hud"
        default=self.compizChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['<Super>','<Ctrl>'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)
     
    def test_reset_display_recent_apps(self):
        schema="com.canonical.Unity.ApplicationsLens"
        key="display-recent-apps"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_boolean(key,False)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_home_lens_ordering(self):
        schema="com.canonical.Unity.Dash"
        key="home-lens-ordering"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['video.lens','music.lens'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)


    def test_dash_form_factoring(self):
        schema="com.canonical.Unity"
        key="form-factor"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_string(key,"Desktop")
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_reset_compiz_scale(self):
        schema="org.compiz.scale"
        key="opacity"
        path="/org/compiz/profiles/unity/plugins/scale/"
        default=self.compizPlugins[schema][key]
        gsettings=Gio.Settings(schema,path)
        gsettings.set_int(key,49)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_enabled_compiz_plugins(self):
        schema="org.compiz.core"
        key="active-plugins"
        path="/org/compiz/profiles/unity/plugins/core/"
        default=self.compizPlugins[schema][key]
        gsettings=Gio.Settings(schema,path)
        gsettings.set_strv(key,['core','composite','opengl','compiztoolbox','decor','vpswitch','snap','mousepoll','resize','place','move','wall','grid','regex','imgpng','session','gnomecompat','animation','fade','unitymtgrabhandles','workarounds','scale','unityshell'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)

    def test_runner_history(self):
        schema="com.canonical.Unity.Runner"
        key="history"
        default=self.unityChildren[schema][key]
        gsettings=Gio.Settings(schema)
        gsettings.set_strv(key,['abc','def'])
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)
   
    def test_launcher_hide_mode(self):
        schema="org.compiz.unityshell"
        key="launcher-hide-mode"
        path="/org/compiz/profiles/unity/plugins/unityshell/"
        default=self.compizPlugins[schema][key]
        gsettings=Gio.Settings(schema,path)
        gsettings.set_int(key,1)
        unityreset.UnityReset(False)
        current=gsettings.get_value(key)
        self.assertTrue(current==default)
      
  
if __name__ == '__main__':
    unittest.main()
