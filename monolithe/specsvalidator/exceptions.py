# -*- coding: utf-8 -*-

class CharacteristicMismatchException:
    def __init__(self, characteristic_name, expected_value, actual_value):
        self.expected_value      = expected_value
        self.actual_value        = actual_value
        self.characteristic_name = characteristic_name

class CharacteristicMissingException:
    def __init__(self, characteristic_name):
        self.characteristic_name = characteristic_name

class MissingDeclarationException:
    def __init__(self, declaration_name):
        self.declaration_name = declaration_name

class ExtraDeclarationException:
    def __init__(self, declaration_name):
        self.declaration_name  = declaration_name

class MispelledDeclarationException:
    def __init__(self, declaration_name, potential_declarations):
        self.declaration_name       = declaration_name
        self.potential_declarations = potential_declarations