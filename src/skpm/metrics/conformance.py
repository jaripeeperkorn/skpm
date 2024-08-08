from sklearn.utils._param_validation import StrOptions
from skpm.config import EventLogConfig as elc

#! CHANGE THIS STILL
class ConformanceMetrics():
    """
    I will implement two methods with each two submethods: Leave-One-Out and Leave_Fraction_Out
    both with single or full cross validation

    Parameters
    ----------
    method : str, default="fraction"
        Whether you want only one control-flow variant in (each) test set or a fraction of the variants
        Possible values: "fraction", "single"
    coverage : str, default="sum"
        Whether you want to take one single test set or multiple experiments where each variant is put into a test set once
        Possible values: "single", "full".
    fraction : float, default="0.1"
        If method == fraction, this indicates the fraction of variants put away in the test set

    Attributes
    ----------
    

    References
    ----------
    [1] Peeperkorn, J., Broucke, S.v. & De Weerdt, J. Can recurrent neural networks learn process model structure?. J Intell Inf Syst 61, 27–51 (2023). 
    [2] Peeperkorn, J., vanden Broucke, S., De Weerdt, J. (2022). Can Deep Neural Networks Learn Process Model Structure? An Assessment Framework and Analysis (2022). 
    

    Examples
    --------
    >>> import numpy as np
    >>> ...

    """

    _parameter_constraints = {
        "method": [
            StrOptions({"fraction", "single"}),
        ],
        "coverage": [
            StrOptions({"single", "full"})      
        ],
    }
    def __init__(self, 
                 method: str = "fraction", 
                 coverage: str = "single", 
                 fraction: float = 0.1)-> None:
        """
        Initialize the ConformanceMetrics.
        """
        self.method = method
        self.coverage = coverage
        self.fraction = fraction
        

        