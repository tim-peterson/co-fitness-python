#from pydoc import help
import scipy
from scipy.stats.stats import pearsonr

#help(pearsonr)
#print scipy.__file__

pval = scipy.stats.stats.combine_pvalues([0.1, 0.2, 0.05])
print pval 
quit()



