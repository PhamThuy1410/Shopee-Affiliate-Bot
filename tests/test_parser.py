from app.utils.parser import parse_shopee_url


def test_product_url():
    url = "https://shopee.vn/product/111222333/444555666"
    result = parse_shopee_url(url)
    assert result["shop_id"] == "111222333"
    assert result["item_id"] == "444555666"


def test_i_url():
    url = "https://shopee.vn/Ao-thun-i.111222333.444555666"
    result = parse_shopee_url(url)
    assert result["shop_id"] == "111222333"
    assert result["item_id"] == "444555666"


def test_invalid_url():
    url = "https://google.com"
    result = parse_shopee_url(url)
    assert result is None