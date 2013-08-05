'''
Created on Aug. 3, 2013

@author: justin.seeley.cn@gmail.com
'''
from distutils.core import setup
import py2exe

setup(
    version="0.0.1",
    description='remove a dir peroidcally',
    name="removeontime",
    # targets to build
    # console = ["RemoveOnTime.py"],
    service=["RemoveOnTime"]
)
