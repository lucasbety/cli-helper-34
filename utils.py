from typing import List, Dict, Any


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (List[List[Any]]): A list containing lists to be flattened.

    Returns:
        List[Any]: A single list containing all elements from the nested lists.
    """
    return [item for sublist in nested_list for item in sublist]


def merge_dicts(dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges a list of dictionaries into a single dictionary.

    Args:
        dicts (List[Dict[str, Any]]): A list of dictionaries to be merged.

    Returns:
        Dict[str, Any]: A single dictionary containing all key-value pairs.
    """
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Divides a list into chunks of a specified size.

    Args:
        data (List[Any]): The list to be divided.
        chunk_size (int): The size of each chunk.

    Returns:
        List[List[Any]]: A list containing chunks of the original list.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
