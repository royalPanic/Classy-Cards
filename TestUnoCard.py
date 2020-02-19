#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
#  testUnoCard.py: unit tests for UnoCard
#  
#  Copyright 2020 Peter Brown <peter.brown@converse.edu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


import unittest
# Import the module(s) you want to test here
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    def test_constructor(self) -> None:
        c:UnoCard = UnoCard('8', 'Red')     # Does it crash?
        c = UnoCard('Skip', 'Blue')
        c = UnoCard('Draw Two', 'Yellow')
        c = UnoCard('0', 'Green')
        c = UnoCard('Draw Four', 'Wild')
        c = UnoCard('', 'Wild')
        self.assertTrue(True)

    

if __name__ == '__main__':
    unittest.main()
