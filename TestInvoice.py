import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_CanCalculateTaxAmount(invoice, products):
    invoice.totalTaxAmount(products)
    assert invoice.totalTaxAmount(products) == 5.2


def test_CanCalculatePriceAfterTax(invoice, products):
    invoice.totalPriceAfterTax(products)
    assert invoice.totalPriceAfterTax(products) == 74.58


def test_CanAddProduct(invoice, products):
    result = invoice.addProduct(4, 4.0, 4)
    product = 'Highlighter'
    products[product] = result
    assert invoice.totalImpurePrice(products) == 91

