import six

from filters.schema import base_query_params_schema
from filters.validations import (
    IntegerLike,
    DatetimeWithTZ
)

# make a validation schema for event filter query params
event_query_schema = base_query_params_schema.extend(
    {
        "name": six.text_type,  # Depends on python version
        "start": DatetimeWithTZ(),
        "org_id": six.text_type,  # Depends on python version
        "cost": IntegerLike(),
    }
)
