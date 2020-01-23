import requests
import xml.etree.ElementTree as et


# def test_check_root_of_xml_response():
#     response = requests.get("http://parabank.parasoft.com/parabank/services/bank/accounts/12345")
#     response_body_as_xml = et.fromstring(response.content)
#     xml_tree = et.ElementTree(response_body_as_xml)
#     root = xml_tree.getroot()
#     assert root.tag == "account"
#     assert len(root.attrib) == 0
#     assert root.text is None
#
#
# def test_check_specific_element_of_xml_response():
#     response = requests.get("http://parabank.parasoft.com/parabank/services/bank/accounts/12345")
#     response_body_as_xml = et.fromstring(response.content)
#     xml_tree = et.ElementTree(response_body_as_xml)
#     first_name = xml_tree.find("customerId")
#     assert first_name.text == "12212"
#
#
# def test_check_number_of_accounts_for_12212_greater_than_five():
#     response = requests.get("http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts")
#     response_body_as_xml = et.fromstring(response.content)
#     xml_tree = et.ElementTree(response_body_as_xml)
#     accounts = xml_tree.findall(".//account")
#     assert len(accounts) < 5


def res():
    response = requests.get("http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts")
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    savings_accounts = xml_tree.findall(".//account/")
    assert len(savings_accounts) > 1


if __name__ == '__main__':
    res()
