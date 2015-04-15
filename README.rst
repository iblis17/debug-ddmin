**************
Software debug
**************

HW2
----

::
 $ cd xmlproc
 $ python ddmin.py
   ERROR: Character data not allowed outside root element at /home/iblis/doc/debug/project2/xmlproc/tmp/tmpfJWCkQ:1:5
   TEXT: ''
   ERROR: Character data not allowed outside root element at /home/iblis/doc/debug/project2/xmlproc/tmp/tmpUhHHSG:1:5
   TEXT: ''
   ERROR: Character data not allowed outside root element at /home/iblis/doc/debug/project2/xmlproc/tmp/tmpavgngy:1:5
   TEXT: ''
   ERROR: Construct started, but never completed at /home/iblis/doc/debug/project2/xmlproc/tmp/tmpG4GKB8:1:5
   TEXT: ''
   ERROR: Character data not allowed outside root element at /home/iblis/doc/debug/project2/xmlproc/tmp/tmpODcrfy:1:3
   TEXT: ''
   =====================================
   found the failed input xmlproc/tmp/tmpiFxfyV
   =====================================
  $ cat tmp/tmpiFxfyV
     <title>Topic Guides &#x04a; python.org</title>
