# Создание xml body
import requests


def fixed_xml_body_as_string():
    return """
    <payee>
        <name>John Smith</name>
        <address>
            <street>My street</street>
            <city>My city</city>
            <state>My state</state>
            <zipCode>90210</zipCode>
        </address>
        <phoneNumber>89126035823</phoneNumber>
        <accountNumber>12345</accountNumber>
    </payee>
    """


def test_send_xml_body_from_string_check_status_code_and_content_type():
    response = requests.post(
        "http://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
        headers={"Content-Type": "application/xml"},
        data=fixed_xml_body_as_string()
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"


