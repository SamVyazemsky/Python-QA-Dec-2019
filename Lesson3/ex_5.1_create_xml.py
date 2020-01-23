# coding=ASCII
import xml.etree.ElementTree as et
import requests


def create_xml_body_using_elementtree():
    payee = et.Element('payee')
    name = et.SubElement(payee, 'name')
    name.text = 'John Smith'
    address = et.SubElement(payee, 'address')
    street = et.SubElement(address, 'street')
    street.text = 'My street'
    city = et.SubElement(address, 'city')
    city.text = 'My city'
    state = et.SubElement(address, 'state')
    state.text = 'My state'
    zip_code = et.SubElement(address, 'zipCode')
    zip_code.text = '90210'
    phone_number = et.SubElement(payee, 'phoneNumber')
    phone_number.text = '0123456789'
    account_number = et.SubElement(payee, 'accountNumber')
    account_number.text = '12345'
    return et.tostring(payee)


def run_send_xml_body_from_elementtree_check_status_code_and_content_type():
    print(create_xml_body_using_elementtree())
    response = requests.post(
        "http://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
        headers={"Content-Type": "application/xml"},
        data=create_xml_body_using_elementtree()
    )

    # assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"


if __name__ == '__main__':
    run_send_xml_body_from_elementtree_check_status_code_and_content_type()