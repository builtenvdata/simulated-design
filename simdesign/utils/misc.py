"""This module provides miscellaneous utility methods.
"""
# Imports from installed packages
import errno
import numpy as np
import os
from pathlib import Path
from time import time, gmtime
from typing import Callable, Union, Any, Dict, List, Mapping
import shutil
import sys
import stat
from inspect import Parameter, signature

PRECISION = 8
"""Precision used in rounding of floating numbers."""


def update_nested_dict(d: Dict[str, Any], u: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively updates a nested dictionary with another dictionary.

    Parameters
    -----------
    d : Dict[str, Any]
        The original nested dictionary to be updated.
    u : Dict[str, Any]
        The dictionary containing updates.

    Returns
    -------
    Dict[str, Any]
        The updated nested dictionary.
    """
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = update_nested_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def run_time(start_time: int) -> str:
    """Print elapsed time between start_time and now in hours, minutes, and
    seconds.

    Parameters
    ----------
    start_time : int
        The initial time obtained via time().

    Returns
    -------
    str
        total run time (hr, min, sec).
    """

    finish_time = time()
    # Procedure to obtained elapsed time in Hr, Min, and Sec
    time_seconds = finish_time - start_time
    time_minutes = int(time_seconds / 60)
    time_hours = int(time_seconds / 3600)
    time_minutes = int(time_minutes - time_hours * 60)
    time_seconds = time_seconds - time_minutes * 60 - time_hours * 3600
    text = (f"Run time: {time_hours:.0f} hours: {time_minutes:.0f} "
            f"minutes: {time_seconds:.2f} seconds")
    print(text)
    return text


def handle_remove_read_only(func: Callable, path: str, exc: tuple) -> None:
    """Grant write permission to a file and remove it using the provided
    function.

    Parameters
    ----------
    func : Callable
        remove function.
    path : str
        file path.
    exc : tuple
        Exception tuple.

    Raises
    ------
    Warning
        Path is in use.
    """
    excvalue: OSError = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise Warning("Path is being used by at the moment.",
                      "It cannot be recreated.")


def remove_dir(dir_path: Union[str, Path]) -> None:
    """Remove a directory if it exists.

    Parameters
    ----------
    dir_path : str | Path
        Name of directory to remove.
    """
    if os.path.exists(dir_path):
        if sys.version_info < (3, 12):
            shutil.rmtree(path=dir_path, onerror=handle_remove_read_only)
        else:
            shutil.rmtree(path=dir_path, onexc=handle_remove_read_only)


def make_dir(dir_path: Union[str, Path]) -> None:
    """Make a clean directory, deleting any existing one first.

    Parameters
    ----------
    dir_path : str | Path
        Name of directory to make.
    """
    if isinstance(dir_path, Path):
        dir_path = str(dir_path)

    if os.path.exists(dir_path):
        remove_dir(dir_path)

    os.makedirs(dir_path)


def signif(x: np.ndarray, p: int) -> np.ndarray:
    """Round an array to the specified number of significant figures.

    Parameters
    ----------
    x : np.ndarray
        array to be rounded.
    p : int
        significant digits.

    Returns
    -------
    np.ndarray
        Rounded array.
    """
    x = np.asarray(x)
    x_positive = np.where(np.isfinite(x) & (x != 0), np.abs(x), 10**(p - 1))
    mags = 10 ** (p - 1 - np.floor(np.log10(x_positive)))
    return np.round(x * mags) / mags


def check_parameters(parameters: dict, required_parameters: tuple) -> None:
    """Check that all required parameters are present in the parameters
    dictionary.

    Parameters
    ----------
    parameters : dict
        user defined parameters.
    required_parameters : tuple
        parameters required by the application.

    Raises
    ------
    KeyError
        A parameter is missing.
    """
    # Check the user entries
    for name in required_parameters:
        if name in parameters.keys():
            continue
        else:
            raise KeyError(f"Required simulation parameter is missing: {name}")


def dot(a: List[float], b: List[float]) -> float:
    """Compute the dot product of two lists of floats.

    Parameters
    ----------
    a : List[float]
        The first list of floats.
    b : List[float]
        The second list of floats.

    Returns
    -------
    float
        Dot product
    """
    if len(a) != len(b):
        return 0.0

    return sum(i[0] * i[1] for i in zip(a, b))


def get_time_based_seed():
    """Return a random seed derived from the current date and time.

    Returns
    -------
    int
        Sum of time components from the current UTC time.
    """
    return sum(gmtime())


def convert_numpy_types(input_list: List[Any]) -> List[Any]:
    """Convert NumPy integer and float types in a list to native Python int
    and float.

    Parameters
    ----------
    input_list : List[Any]
        A list containing elements that may include NumPy-specific types or
        standard Python types.

    Returns
    -------
    List[Any]
        A new list with NumPy types converted to their corresponding Python
        types (`int` or `float`). Non-NumPy types are returned unchanged.

    Example
    -------
    >>> example_list = [np.float64(3.14), np.int32(10), 5, 7.2]
    >>> convert_numpy_types(example_list)
    [3.14, 10, 5, 7.2]
    """
    result = []
    for item in input_list:
        if isinstance(item, np.integer):  # Check for NumPy int type
            result.append(int(item))
        elif isinstance(item, np.floating):  # Check for NumPy float type
            result.append(float(item))
        else:
            result.append(item)  # Keep as is if it's not a NumPy type

    return result


def round_list(input_list: List[Any],
               precision: int = PRECISION) -> List[Any]:
    """Round each value in a list to the specified precision.

    Parameters
    ----------
    input_list : List[Any]
        A list of floating-point numbers to be rounded.
    precision : int
        Number of decimal places, by default equal to the constant
        ``PRECISION``.

    Returns
    -------
    List[Any]
        A new list with each value rounded to the specified precision.

    Examples
    --------
    >>> round_list([3.14159, 2.71828, 1.61803], 2)
    [3.14, 2.72, 1.62]
    """
    input_list = convert_numpy_types(input_list)
    return [
        round(value, precision) if isinstance(value, (int, float)) else value
        for value in input_list
    ]


def filter_args(method: Callable, data: Mapping[str, Any]) -> Dict[str, Any]:
    """Filter and convert input values so they match the signature of a method.

    Parameters
    ----------
    method : callable
        The method whose signature is used for filtering and conversion.

    data : Mapping[str, Any]
        A dictionary-like object containing raw input values (e.g., JSON body,
        query parameters, or user-provided input). Keys are expected to match
        parameter names of the method.

    Returns
    -------
    dict[str, Any]
        A dictionary containing only the parameters expected by `method`,
        with types converted based on annotations when possible. If `method`
        defines ``**kwargs``, extra keys in `data` are also included so they
        can be passed through via ``**filtered_data``.
    """
    params = dict(signature(method).parameters)
    filtered_data: Dict[str, Any] = {}

    # Does the method accept **kwargs?
    has_var_kw = any(p.kind is Parameter.VAR_KEYWORD for p in params.values())

    # Handle all explicitly declared parameters (except *args/**kwargs/self)
    for name, param in params.items():
        if name == "self":
            continue

        if param.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
            continue

        has_default = param.default is not Parameter.empty
        is_provided = name in data

        # Missing value
        if not is_provided:
            if has_default:
                filtered_data[name] = param.default
            # If no default and not provided, skip
            continue

        raw_value = data[name]
        annotation = param.annotation

        # Handle bool explicitly
        if annotation is bool:
            try:
                filtered_data[name] = str(raw_value).lower() == "true"
            except Exception:
                filtered_data[name] = raw_value

        # Handle integers
        elif annotation is int:
            try:
                filtered_data[name] = int(raw_value)
            except (ValueError, TypeError):
                filtered_data[name] = raw_value

        # Handle floats
        elif annotation is float:
            try:
                filtered_data[name] = float(raw_value)
            except (ValueError, TypeError):
                filtered_data[name] = raw_value

        # For any other annotation (or no annotation), just pass through
        else:
            filtered_data[name] = raw_value

    # If the method accepts **kwargs, forward any extra keys from `data`
    if has_var_kw:
        # Names of "real" positional/keyword parameters that we already handled
        known_param_names = {
            n
            for n, p in params.items()
            if n != "self" and p.kind not in (Parameter.VAR_POSITIONAL,
                                              Parameter.VAR_KEYWORD)
        }

        for key, value in data.items():
            if key not in known_param_names:
                # Extra keys go straight through (no conversion, no filtering)
                filtered_data[key] = value

    return filtered_data
