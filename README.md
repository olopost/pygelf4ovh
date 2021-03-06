# pygelf4ovh
pygelf adaptation that work for OVH Logs Data Platform


[![GitHub issues](https://img.shields.io/github/issues/olopost/pygelf4ovh)](https://github.com/olopost/pygelf4ovh/issues)
[![GitHub forks](https://img.shields.io/github/forks/olopost/pygelf4ovh)](https://github.com/olopost/pygelf4ovh/network)
[![GitHub stars](https://img.shields.io/github/stars/olopost/pygelf4ovh)](https://github.com/olopost/pygelf4ovh/stargazers)
[![GitHub license](https://img.shields.io/github/license/olopost/pygelf4ovh)](https://github.com/olopost/pygelf4ovh/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Folopost%2Fpygelf4ovh)



## Install
Just use pypi repository
~~~bash
pip install pygelf4ovh
~~~

## Usage

Just add GelfOVHHandler in logging handler

~~~python
#import pygelf4ovh
import pygelf4ovh
import logging
OVH_URL = 'gra2.logs.ovh.com'
OVH_PORT = 2202
OVH_TOKEN = "your ovh api token"
from pygelf4ovh import GelfOVHHandler

logger = logging.getLogger('mylog')
logger.setLevel(logging.INFO)
sh = GelfOVHHandler(host=OVH_URL,
                   port=OVH_PORT, ovh_token=OVH_TOKEN,
                   include_extra_fields=True,
                   debug=True)
logger.addHandler(sh)

# now your handler work as usual
logger.info("my info log")

~~~

## Some warn
Pygelf4ovh has been only tested with python3

## Release note
 - Version 0.4
  * Solved issue : [issue #1](https://github.com/olopost/pygelf4ovh/issues/1)
 - Version 0.3
   * Add some doc
 - Version 0.2
   * Test done on OVH  Platform 
   * Thanks to : Ivan Mukhin for PyGelf : [PyGelf GitHub project](https://github.com/keeprocking/pygelf)
   
 - Version 0.1
   * Initial commit - first working version