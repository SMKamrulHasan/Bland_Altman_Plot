#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyCompare
import numpy as np
import matplotlib.pyplot as plt


"""

Myocardial Mass ED

"""

auto_ED_Myo_Mass = np.array([183349.609375
,181792.96875
,182976.822669983
,60789.55078125
,156115.72265625
,157034.118652344
,95858.3605499268
,125610.3515625
,146155.725517273
,66088.8671875
,105493.1640625
,95166.015625
,102083.472846985
,94833.6481323242
,73320.6992340088

])


manual_ED_Myo_Mass = np.array([164257.8125
,183691.40625
,188135.83820343
,70459.716796875
,176676.940917969
,187925.354003906
,92289.4210891724
,137386.322021484
,132912.886299133
,65502.9296875
,98706.0546875
,106298.828125
,97772.5845108032
,93511.6177215576
,68698.119140625
])

pyCompare.blandAltman(auto_ED_Myo_Mass, manual_ED_Myo_Mass, limitOfAgreement=1.96,  confidenceInterval=95, title='Myo Mass ED (g)   rho=0.96',meanColour='c', loaColour='gray', pointColour='red',dpi=1000,savePath='bland_MyoMassED.png')



