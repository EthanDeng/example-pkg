import pandas as pd
import numpy as np


def corr_shift(x, y, x_shift=0, y_shift=0):
    """compute the correlation with shift

    Args:
        x (series): first series
        y (series): second series
        x_shift (int, optional): shift of first series. Defaults to 0.
        y_shift (int, optional): shift of second series. Defaults to 0.

    Returns:
        float: correlation
    """
    return x.shift(x_shift).corr(y.shift(y_shift))


def shift(df, shift_map=None):
    """shift the dataframe

    Args:
        df (dataframe): origin dataframe
        shift_map (dict, optional): mapping of shift for columns of dataframe. Defaults to None.

    Returns:
        dataframe: shiftted dataframe
    """
    if shift_map is not None:
        df = df.copy()
        min_lag = min(0, min(shift_map.values()))
        max_lead = max(0, max(shift_map.values()))
        df = df.reindex(df.index.union(df.index.shift(min_lag)).union(df.index.shift(max_lead)))
        for k, v in shift_map.items():
            df[k] = df[k].shift(v)
        return df
    else:
        return df