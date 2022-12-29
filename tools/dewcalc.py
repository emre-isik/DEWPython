import numpy as np
import DEWPython
from DEWPython import DEWModel as dm
import sys

#inFile = sys.argv[1]
#outFile = sys.argv[2]

reaction = dm.DEW()

pt_arr = [[100,1200,1], [1,60,1]] # temp (C), press (kb)

#with open(inFile,'r') as i:
#    lines = i.readlines()

#print(lines)

reaction.run(pt_arr, min_inp =[], aq_inp = [['CO2,aq', '1'], ['H2,aq', '4']], g_inp = [], h2o_inp = 0, min_out = [],aq_out =[['METHANE,AQ','1']], g_out = [], h2o_out = 2, ptInp = 'Regular', rhoWat = 'Z&D 2005', forceBool = False, dieEQ = 'Sverjensky', forceSC = False, WFEQ ='D&H 1978', dsV = False, pdsV = False, DV = False, makePlots = False)

reaction.export_to_csv()
