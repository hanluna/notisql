from dataclasses import dataclass


@dataclass
class Model(order=True, unsfafe_hash=True):
    """
    For more information: https://github.com/hannbyul/notisql/issues/2#issuecomment-1478729429
    """

    parent: dict
    id: str
    created_time: str
    created_by: dict
    last_edited_time: str
    last_edited_by: dict
