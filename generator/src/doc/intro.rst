Package structure
=================

VSDK is automatically generated from the VSD ReST API source code. The
generated code is part of the :mod:`vsdk.autogenerates` package. Every
generated class can be overriden in the corresponding module. For example
:class:`vsdk.autogenerates.nuaddressrange.NUAddressRange` is overriden by
:class:`vsdk.nuaddressrange.NUAddressRange`

The :mod:`vsdk.fetchers` package is automatically auto-generated as well and
should not be used directly.

The :mod:`vsdk.utils` module contains a few utilities (logging).
