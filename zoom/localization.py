# -*- coding: utf-8 -*-
#
# Zoom - gedit plugin
# Copyright (C) 2010 Christian Luginbühl
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gettext import install
from os.path import join, dirname

class Localization():
    """ Provides a helper to easily setup l10n. """

    _initialized = False

    _domain = "messages"
    _locale_path = join(dirname(__file__), "locale")

    @classmethod
    def setup(self):
        """ Sets up the gettext localization. """

        if (not self._initialized):
            install(self._domain, self._locale_path)
            self._initialized = True
