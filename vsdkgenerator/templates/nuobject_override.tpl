# -*- coding: utf-8 -*-

"""
NU{{ model['name'] }}
{{ model['description'] }}

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from .autogenerates import NU{{ model['name'] }} as AutoGenerate


class NU{{ model['name'] }}(AutoGenerate):
    """ Represents a {{ model['name'] }} object in the VSD
        {{ model['description'] }}

        This object should contain all NU{{ model['name'] }} specific methods

    """

    def __init__(self, **kwargs):
        """ Initializing a NU{{ model['name'] }} """

        super(NU{{ model['name'] }}, self).__init__(kwargs)
        pass
