#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import re


def str2list(strlist):
    """Convert key1,key2,... string into list.
    :param strlist: key1,key2
    strlist can be comma or space separated.
    """
    if strlist is not None:
        strlist = strlist.strip(', ')
    if not strlist:
        return []
    return re.split("[, ]+", strlist)
