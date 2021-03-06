# Copyright 2005-2010 Wesabe, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from fixofx.ofx import Response
from fixofx.test.ofx_test_utils import get_checking_stmt


class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.checking = get_checking_stmt()
    
    def test_statement_as_xml(self):
        response = Response(self.checking)
        self.assertEqual('<?xml version="1.0"', response.as_xml()[:19])
    

if __name__ == '__main__':
    unittest.main()
