# -*- coding: utf-8 -*-
"""
DreamPlex Plugin by DonDavici, 2012
 
https://github.com/DonDavici/DreamPlex

Some of the code is from other plugins:
all credits to the coders :-)

DreamPlex Plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

DreamPlex Plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
"""
#===============================================================================
# IMPORT
#===============================================================================
from Components.config import config

from __common__ import printl2 as printl

#===============================================================================
# DEPRECATED FOR NOW
#===============================================================================
def getPictureData(details, prefix, postfix, usePicCache):
	printl("", __name__, "S")
	
	if details["ratingKey"] is None or details["ratingKey"] == "None" or details["ratingKey"] == "":
		target = "None"
	else:
		if usePicCache:
			mediaPath = config.plugins.dreamplex.mediafolderpath.value
			name = details["ratingKey"]
		else:
			mediaPath = config.plugins.dreamplex.logfolderpath.value
			name = "temp"
		try:

			target = mediaPath + prefix + "_" + name + postfix
			printl( "target: " + str(target), __name__, "D")
		except:
			target = "/usr/lib/enigma2/python/Plugins/Extensions/DreamPlex/skins/" + config.plugins.dreamplex.skins.value + "/all/picreset.png"
			printl( "something went wrong", __name__, "D")
	
	printl("", __name__, "C")
	return target	
	