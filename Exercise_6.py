import pandas as pd 
import numpy as np

labresults = pd.DataFrame({ 
    "sampleid": ["S01", "S02", "S03", "S04", "S05", "S06"], 
    "hemoglobin": [13.2, 14.1, np.nan, 12.8, np.nan, 15.0], 
    "crp": [2.1, np.nan, 8.4, 3.2, 12.5, np.nan] 
})