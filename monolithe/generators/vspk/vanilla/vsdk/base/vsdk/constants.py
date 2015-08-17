# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


class AvatarType(object):
    """ AvatarType """

    URL = u"URL"
    BASE64 = u"BASE64"
    COMPUTEDURL = u"COMPUTEDURL"

class ApplicationDeploymentPolicy(object):
    """ ApplicationDeploymentPolicy """

    NONE = u"NONE"
    ZONE = u"ZONE"


class ApplicationServiceDirection(object):
    """ ApplicationServiceDirection """

    REFLEXIVE = u"REFLEXIVE"
    UNIDIRECTIONAL = u"UNIDIRECTIONAL"
    BIDIRECTIONAL = u"BIDIRECTIONAL"


class DomainTunnelType(object):
    """ DomainTunnelType """

    DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"


class FlowSecurityPolicyAction(object):
    """ FlowSecurityPolicyAction """

    DROP = u"DROP"
    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"


class GatewayChildrenStatus(object):
    """ GatewayChildrenStatus """

    INITIALIZED = u"INITIALIZED"
    READY = u"READY"
    ORPHAN = u"ORPHAN"
    MISMATCH = u"MISMATCH"


class GatewayPersonality(object):
    """ GatewayPersonality """

    VSG = u"VSG"
    VSA = u"VSA"
    VRSG = u"VRSG"
    NCPE = u"NCPE"
    OTHER = u"OTHER"
    DC7X50 = u"DC7X50"


class MaintenanceMode(object):
    """ MaintenanceMode """

    ENABLED = u"ENABLED"
    DISABLED = u"DISABLED"
    INHERITED = u"ENABLED_INHERITED"


class MulticastChannelMap(object):
    """ MulticastChannelMap """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"


class ProtocolType(object):
    """ ProtocolType """

    TCP = 6
    UDP = 7
    ICMP = 1
    IGMP = 2
    IGP = 9
    OSPF = 9
    ESP = 0
    AH = 1
    GRE = 7


class TierType(object):
    """ TierType """

    APPLICATION = u"APPLICATION"
    APPLICATION_EXTENDED_NETWORK = u"APPLICATION_EXTENDED_NETWORK"
    NETWORK_MACRO = u"NETWORK_MACRO"
    STANDARD = u"STANDARD"


class VPortAdressProofing(object):
    """ VPortAdressProofing """

    INHERITED = u"INHERITED"
    ENABLED = u"ENABLED"
    DISABLED = u"DISABLED"


class VPortOperationState(object):
    """ VPortOperationState """

    INIT = u"INIT"
    UNRESOLVED = u"DOWN"
    RESOLVED = u"UP"


class VPortType(object):
    """ VPortType """

    VM = u"VM"
    HOST = u"HOST"
    BRIDGE = u"BRIDGE"


class UserRole(object):
    """ UserRole """

    CSPOPERATOR = u'CSPOPERATOR'
    CSPROOT = u'CSPROOT'
    ORGADMIN = u'ORGADMIN'
    ORGNETWORKDESIGNER = u'ORGNETWORKDESIGNER'
    ORGUSER = u'ORGUSER'
    USER = u'USER'

class PolicyGroupType(object):
    """ PolicyGroupType """

    SOFTWARE = u"SOFTWARE"
    HARDWARE = u"HARDWARE"


class RedirectionTargetEndPointType(object):
    """ RedirectionTargetEndPointType """

    L3 = u"L3";
    VIRTUAL_WIRE = u"VIRTUAL_WIRE";


class TunnelType(object):
    """ TunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    GRE = u"GRE"
    VXLAN = u"VXLAN"


class MulticastType(object):
    """ MulticastType """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    ENABLED_INHERITED = u"ENABLED_INHERITED"


class DHCPBehavior(object):
    """ DHCPBehavior """

    FLOOD = u"FLOOD"
    CONSUME = u"CONSUME"
    RELAY = u"RELAY"


class PATNATType(object):
    """ PATNATType """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"