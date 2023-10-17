#!/usr/bin/env python

# cat 异常测试自动化平台设计方案.md| grep image | awk -F"/" '{print $2}' | sed 's/)//g' > file.txt
#
#
import os
no_remove = set()
with open('./file.txt') as f:
     for line in f:
         no_remove.add(line.strip())

for f in os.listdir('.'):
    if f not in no_remove:
        print('unlink:' + f ) 
        os.unlink(f)
