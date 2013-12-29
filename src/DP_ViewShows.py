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

from DP_ViewCine import DP_ViewCine

from __common__ import printl2 as printl

#===============================================================================
# 
#===============================================================================
def getViewClass():
	printl("",__name__ , "S")
	
	printl("",__name__ , "C")
	return DPS_ViewShows

#===============================================================================
# 
#===============================================================================
class DPS_ViewShows(DP_ViewCine):

	parentSeasonId = None

	#===========================================================================
	# 
	#===========================================================================
	def __init__(self, session, libraryName, loadLibrary, playEntry, viewName, select=None, sort=None, myFilter=None, cache=None):
		printl("", self , "S")

		self.session = session
		DP_ViewCine.__init__(self, session, libraryName, loadLibrary, playEntry, viewName, select, sort, myFilter, cache)

		printl("", self, "C")

	#===========================================================================
	# 
	#===========================================================================
	def getPictureInformationToLoad(self):
		printl("", self, "S")
		printl("viewMode: " + str(self.details ["viewMode"]), self, "D")

		# TODO change backdrop and poster usage via self.myParams["elements"]["backdrop"]["visible"]

		if self.details ["viewMode"] == "ShowSeasons":
			printl( "is ShowSeasons", self, "D")
			self.parentSeasonId = self.details ["ratingKey"]
			self.isTvShow = True
			self.startPlaybackNow = True
			self.bname = self.details["ratingKey"]
			self.pname = self.details["ratingKey"]
			self.changeBackdrop = True
			self.changePoster = True
			self.resetPoster = True
			self.resetBackdrop = True
	
		elif self.details ["viewMode"] == "ShowEpisodes" and self.details["ratingKey"] == "0":
			printl( "is ShowEpisodes all entry", self, "D")
			self.isTvShow = True
			self.bname = self.parentSeasonId
			self.pname = self.parentSeasonId
			self.startPlaybackNow = False
			self.changeBackdrop = True
			self.changePoster = True
			self.resetPoster = False
			self.resetBackdrop = False
			
		elif self.details ["viewMode"] == "ShowEpisodes" and self.details["ratingKey"] != "":
			printl( "is ShowEpisodes special season",self, "D")
			self.isTvShow = True
			self.parentSeasonNr = self.details["ratingKey"]
			self.bname = self.parentSeasonId
			self.pname = self.details["ratingKey"]
			self.startPlaybackNow = False
			self.changeBackdrop = False
			self.changePoster = True
			self.resetPoster = False
			self.resetBackdrop = False

		elif self.details["viewMode"] == "directMode":
			printl( "is directMode",self, "D")
			self.startPlaybackNow = True
			#self.isTvShow = True
			self.bname = self.details["ratingKey"]
			self.pname = self.extraData["grandparentRatingKey"]
			self.changeBackdrop = self.myParams["elements"]["backdrop"]["visible"]
			self.changePoster = self.myParams["elements"]["poster"]["visible"]
			self.resetPoster = True
			self.resetBackdrop = True

		else:
			printl( "is playable content",self, "D")
			self.bname = self.details["ratingKey"]
			self.startPlaybackNow = False

			if self.parentSeasonId is not None:
				self.pname = self.parentSeasonId
			else:
				self.pname = self.extraData["parentRatingKey"]
			# we dont want to have the same poster downloaded and used for each episode
			self.changePoster = False
			self.changeBackdrop = True

		if not self.usePicCache:
			self.pname = "temp"
			self.bname = "temp"
			self.mediaPath = config.plugins.dreamplex.logfolderpath.value

		printl("bname: " + str(self.bname), self, "D")
		printl("pname: " + str(self.pname), self, "D")
		self.whatPoster = self.mediaPath + self.image_prefix + "_" + self.pname + self.poster_postfix
		self.whatBackdrop = self.mediaPath + self.image_prefix + "_" + self.bname + self.backdrop_postfix

		printl("self.whatPoster : " + str(self.whatPoster ), self, "D")
		printl("self.whatBackdrop: " + str(self.whatBackdrop), self, "D")

		printl("", self, "C")

	#===========================================================================
	#
	#===========================================================================
	def onEnter(self):
		printl("", self, "S")

		# first we call the the rest of the onEnter from super
		super(DPS_ViewShows,self).onEnter()

		# this is the part we extend
		if self.viewMode == "ShowSeasons" or self.viewMode == "ShowEpisodes":
			self.processGuiElements(self.viewMode)

		printl("", self, "C")

	#===========================================================================
	#
	#===========================================================================
	def onLeave(self):
		printl("", self, "S")

		# first we call the the rest of the onEnter from super
		super(DPS_ViewShows,self).onLeave()

		self.restoreElementsInViewStep()

		printl("", self, "C")
