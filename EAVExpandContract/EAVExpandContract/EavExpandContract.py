# -*- coding: utf-8 -*-
"""

use expandEAV to take an EAV DataFrame and convert to a schema table
use compressToEAV to take a schema DataFrame to an EAV table
routines originally written in VBA for MS Excel by Jim Sullivan
converted to python by Jim Sullivan

"""

import pandas as pd
import numpy as np

def expandEAV(eavdf):
    #They must send an EAV table else we do nothing
    if eavdf.shape[1]!=3:
        print("You sent a DataFrame that contains " + str(eavdf.shape[1]) +\
              " columns.  We expected 3.  We're returning the original " +\
              "DataFrame unaltered.")
        return eavdf
    
    #there must be at least one record in the table else nothing
    if eavdf.shape[0]<1:
        print("You sent a DataFrame with no records.  No action taken")
        return eavdf
    
    #create an empty destination dataFrame to hold the expanded matrix
    destdf = pd.DataFrame()
    #the column of the EAV for entity or row is the zero index column
    ercol = list(eavdf)[0]
    #the unique records will become the row indices
    srec=eavdf.loc[:,ercol].unique()
    for row in srec:
        destdf.loc[row,:]=np.NaN
    
    #the index one column of the EAV contains the attributes / fields    
    afcol = list(eavdf)[1]
    #the list of unique attributes will be the column headers
    scol=eavdf.loc[:,afcol].unique()
    for col in scol:
        destdf.loc[:,col]=np.NaN
    
    #for each eav tuple, populate the destination table
    for srindex in eavdf.itertuples():
        ser = srindex[1]
        saf = srindex[2]
        svm = srindex[3]
        
        destdf.loc[ser, saf]=svm
        
    #print("Here is the DataFrame we're returning:")
    #print(destdf)
    
    return destdf

def compressToEAV(schemadf):
    if schemadf.shape[0]<1:
        print("You send a DataFrame with no records.  No action taken")
        return schemadf
    
    destdf = pd.DataFrame()
    destdf.loc[:,'entity']=[]
    destdf.loc[:,'attribute']=[]
    destdf.loc[:,'value']=[]
    drindex=0
    for e in schemadf.index:
        for a in schemadf.columns:
            if str(schemadf.loc[e,a]) != 'nan':
                destdf.loc[drindex,:]=[e,a,schemadf.loc[e,a]]
                drindex += 1
    #print("Returning the following EAV table:")
    #print(destdf)
    return destdf

        
def main():
    
    sdf = pd.DataFrame()
    sdf.loc[:,'row']=['a','a','x','z','v','z','y','z','b']
    sdf.loc[:,'col']=['this','that','the','other','the','the','the','a','a']
    sdf.loc[:,'val']=[4,3,2,5,9,5,6,5,4]
    
    print("EAV matrix fed to expander:")
    print(sdf)
    
    ddf = expandEAV(sdf)
    
    print("Expanded Matrix:")
    print(ddf)
    
    print("Now passing it back to the compression routine")
    neweav = compressToEAV(ddf)
    print(neweav)
    
    
    

if __name__ == "__main__": main()