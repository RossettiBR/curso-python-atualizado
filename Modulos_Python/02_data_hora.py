from datetime import datetime
from pytz import timezone

data = datetime(2023, 5, 24)
print(data)

data_hj = datetime.now(timezone('America/Sao_Paulo'))
print(data_hj)
