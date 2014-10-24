# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Chiriin3D_reverse
                                 A QGIS plugin
 This plugin reverses a Chiriin Chizu 3D model.
                             -------------------
        begin                : 2014-10-24
        copyright            : (C) 2014 by Takayuki Mizutani
        email                : mizutani.takayuki@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Chiriin3D_reverse class from file Chiriin3D_reverse.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .chiriin3d_reverse import Chiriin3D_reverse
    return Chiriin3D_reverse(iface)
