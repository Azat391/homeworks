import pytest
def get_initial_data():
    return {
    "id": 1,
    "items": ["book", "pen"],
}
@pytest.fixture
def user_account():
    return {
    "name": "test_user",
    "balance": 100,
    }

@pytest.fixture
def app_config():
    return {
    "url": "http://test.com",
    "debug": False,
}
def test_debug_mode_is_disabled(app_config):
    assert app_config['debug']==False

@pytest.fixture
def product_item():
    return {
    "name": "Laptop",
    "price": 1500,
    "in_stock": True,
}
def test_product_in_stock(product_item):
    assert product_item['in_stock']==True

@pytest.fixture
def sample_order():
    return {
    "order_id": 42,
    "amount": 99.90,
    "currency": "USD",
}
def test_order_id(sample_order):
    assert sample_order['order_id']==42
def test_order_currency(sample_order):
    assert sample_order['currency']=='USD'

@pytest.fixture
def http_headers():
    return  {
    "content-type": "text/html; charset=utf-8",
    "date": "Wed, 14 Oct 2026 09:12:57 GMT",
    "ga-ap": "eu-central-1",
    "set-cookie": "x-ap=eu-central-1; Path=/; SameSite=lax",
    "transfer-encoding": "chunked",
    "vary": "Accept-Encoding",
    "x-frame-options": "SAMEORIGIN"
}
def test_content_type_header(http_headers):
    assert http_headers['content-type']=='text/html; charset=utf-8'

class Player():
    def __init__(self, name, level):
        self.name=name
        self.level=level
@pytest.fixture
def new_player():
    return Player('Gandalf', 99)

class Order():
    def __init__(self,list):
        self.list=list
    def list_add(self,name):
        self.list.append(name)
@pytest.fixture
def order_with_items():
    list1=Order([])
    list1.list_add('sword')
    list1.list_add('shield')
    return list1
def test_list1(order_with_items):
    assert 'sword' in order_with_items.list #.list в конце это нейрохрючево, я сам не догадался к атрибуту этому обратиться

@pytest.fixture
def api_response():
    return {
    "status_code": 200,
    "data": "Success",
}
def test_api_response(api_response):
    assert api_response['status_code']==200
