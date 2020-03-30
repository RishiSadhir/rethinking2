import rchitect as R
import pandas as pd


def data_from_R(dataset, package):
    """
    Import datasets from R.

    This is basically a wrapper around R's `data`
    function in the base library.

    https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/data
    """
    s = f"data({dataset}, package = \"{package}\")"
    R.reval(s)
    d = R.reval(f"{dataset}")
    df = R.rcopy(d)
    return pd.DataFrame(df)
