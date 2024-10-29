import keyword
from pprint import pprint
import random
from enum import Enum

import json


class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'


response = '''{
    "status":"ok"
}'''

data = json.loads(response)
status = data['status']

try: 
    if ResponseStatus(status) is ResponseStatus.FULFILLED:
        print(ResponseStatus(status))
        print('The request completed successfully')
except ValueError as error:
    print(error)