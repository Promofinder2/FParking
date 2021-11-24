import fastapi
import pydantic
from typing import Optional
from collections import OrderedDict

class FlashReceipt(pydantic.BaseModel):
    DataName: Optional[str]
    DataLocation : Optional[str]
    DataCity : Optional [str]
    DataArrival : Optional[str]
    DataDeparture : Optional[str]
    DataPayment : Optional[str]
    DataReceipt : Optional[str]

class Config(FlashReceipt):
    allow_mutation = True