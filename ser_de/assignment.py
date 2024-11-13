import json
from datetime import date, datetime
from decimal import Decimal
from marshmallow import Schema, fields

class Stock:
    def __init__(self, symbol, date, open, high, low, close, volume, object_type='Stock'):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.object_type='Stock'
    
    def to_json(self):
        return vars(self)
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission, object_type='Trade'):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
        self.object_type='Trade'

    def to_json(self):
        return vars(self)

class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, date) and type(arg) == date:
            return arg.strftime('%Y-%m-%d')
        if isinstance(arg, datetime) and type(arg) == datetime:
            return arg.strftime('%Y-%m-%dT%H:%M:%S')
        if isinstance(arg, Decimal):
            return str(arg)
        if isinstance(arg, Stock) or isinstance(arg, Trade):
            return arg.to_json()  # Ensure to_json returns a dict with all fields
        return super().default(arg)

def custom_decoder(arg):
    """Deserialize JSON objects into Stock or Trade instances."""
    if 'object_type' in arg   and  arg['object_type']=='Stock':  # Check for Stock attributes
        return Stock(
            symbol=arg['symbol'],
            date=datetime.strptime(arg['date'], '%Y-%m-%d').date(),
            open=Decimal(str(arg['open'])),
            high=Decimal(str(arg['high'])),
            low=Decimal(str(arg['low'])),
            close=Decimal(str(arg['close'])),
            volume=arg['volume']
        )
    elif 'object_type' in arg   and  arg['object_type']=='Trade':  # Check for Trade attributes
        return Trade(
            symbol=arg['symbol'],
            timestamp=datetime.strptime(arg['timestamp'], '%Y-%m-%dT%H:%M:%S'),
            order=arg['order'],
            price=Decimal(str(arg['price'])),
            volume=arg['volume'],
            commission=Decimal(str(arg['commission']))
        )
    return arg  # Return the original argument if it doesn't match

class StockSchema(Schema):
    symbol = fields.String()
    date = fields.Date(format='%Y-%m-%d')
    open = fields.Float()
    high = fields.Float()
    low = fields.Float()
    close = fields.Float()
    volume = fields.Int()
    object_type = fields.Str()

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Float()
    commission = fields.Float()
    volume = fields.Int()
    object_type = fields.Str() 

def serialize_with_marshmallow(obj):
    if obj.object_type=='Stock':
        stock_schema=StockSchema()
        return stock_schema.dumps(obj)
    elif obj.object_type=='Trade':
        trade_schema=TradeSchema()
        return trade_schema.dumps(obj)
    return obj

# serialize_with_marshmallow(activity["quotes"][0])
def deserialize_with_marshmallow(obj, schema):
    """Deserialize a JSON string into a Stock or Trade object using Marshmallow."""
    if schema.__class__ == StockSchema:
        data = schema.loads(obj)  # Deserialize into a dictionary
        return Stock(**data)  # Create and return a Stock instance
    elif schema.__class__ == TradeSchema:
        data = schema.loads(obj)  # Deserialize into a dictionary
        return Trade(**data)  # Create and return a Trade instance
    return None  # Return None if schema is not recognized

