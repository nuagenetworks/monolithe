# -*- coding:utf-8 -*-

from restnuage import NURESTObject

NUGATEWAY_PERSONALITYVSG = u"VSG"
NUGATEWAY_PERSONALITYVSA = u"VSA"
NUGATEWAY_PERSONALITYVRSG = u"VRSG"
NUGATEWAY_PERSONALITYNCPE = u"NCPE"
NUGATEWAY_PERSONALITYOTHER = u"OTHER"
NUGATEWAY_PERSONALITYDC7X50 = u"DC7X50"


class NUGatewayBase(NURESTObject):
    """ Defines a gateway base """

    def __init__(self):
        """ Initialize a new object """

        super(NUGatewayBase, self).__init__()

        # Read/Write Attributes
        self.description = None
        self.name = None
        self.personality = None

        self.expose_attribute(local_name=u'descritpion')
        self.expose_attribute(local_name=u'name')
        self.expose_attribute(local_name=u'personality')
