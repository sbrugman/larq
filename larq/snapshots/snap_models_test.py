# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_summary 1'] = '''+sequential stats----------------------------------------------------------------------------------------------------------------+
| Layer                   Input prec.           Outputs  # 1-bit  # 2-bit  # 32-bit  Memory  1-bit MACs  2-bit MACs  32-bit MACs |
|                               (bit)                        x 1      x 1       x 1    (kB)                                      |
+--------------------------------------------------------------------------------------------------------------------------------+
| quant_conv2d                      -  (-1, 64, 64, 32)      288        0        32    0.16           0           0      1179648 |
| max_pooling2d                     -  (-1, 32, 32, 32)        0        0         0       0           0           0            0 |
| quant_depthwise_conv2d            2  (-1, 11, 11, 32)        0      288         0    0.07           0       34848            0 |
| quant_separable_conv2d            1  (-1, 11, 11, 32)     1312        0        32    0.29      158752           0            0 |
| flatten                           -        (-1, 3872)        0        0         0       0           0           0            0 |
| dense                             -          (-1, 10)        0        0     38730  151.29           0           0        38720 |
+--------------------------------------------------------------------------------------------------------------------------------+
| Total                                                     1600      288     38794  151.80      158752       34848      1218368 |
+--------------------------------------------------------------------------------------------------------------------------------+
+sequential summary--------------------------+
| Total params                       40.7 k  |
| Trainable params                   1.95 k  |
| Non-trainable params               38.7 k  |
| Model size                         0.15 MB |
| Float-32 Equivalent                0.16 MB |
| Compression Ratio of Memory        0.96    |
| Number of MACs                     1.41 M  |
| Ratio of MACs that are binarized   0.1124  |
| Ratio of MACs that are ternarized  0.0247  |
+--------------------------------------------+
'''

snapshots['test_save_summary 1'] = '''Layer,Input prec. (bit),Outputs,# 1-bit x 1,# 2-bit x 1,# 32-bit x 1,Memory (kB),1-bit MACs,2-bit MACs,32-bit MACs\r
quant_conv2d,-,"(-1, 64, 64, 32)",288,0,32,0.16015625,0,0,1179648\r
max_pooling2d,-,"(-1, 32, 32, 32)",0,0,0,0,0,0,0\r
quant_depthwise_conv2d,2,"(-1, 11, 11, 32)",0,288,0,0.0703125,0,34848,0\r
quant_separable_conv2d,1,"(-1, 11, 11, 32)",1312,0,32,0.28515625,158752,0,0\r
flatten,-,"(-1, 3872)",0,0,0,0,0,0,0\r
dense,-,"(-1, 10)",0,0,38730,151.2890625,0,0,38720\r
Total,,,1600,288,38794,151.8046875,158752,34848,1218368\r
\r
Total params,Trainable params,Non-trainable params,Model size,Float-32 Equivalent,Compression Ratio of Memory,Number of MACs,Ratio of MACs that are binarized,Ratio of MACs that are ternarized\r
40.7 k,1.95 k,38.7 k,0.15 MB,0.16 MB,0.9552627697753306,1.41 M,0.1124,0.0247\r
'''
