import email
import imaplib
import time
from email.header import decode_header

import pytest
from selenium import webdriver

from PageObjects.SignupPageHubspot import signup
from TestData.gmailcredentials import credentials
from Utilities.utilityHubspot import hubspotBaseclass


class TestVerifyOTP(hubspotBaseclass):
    driver: webdriver  # type hinting

    # Register on hubspot, integrate with gmail and verify with an OTP
    def test_verify_OTP(self, get_credentials):

        register = signup(self.driver)
        register.emailbox().clear()

        email_address = get_credentials["email"]
        password = get_credentials["pw"]

        register.emailbox().send_keys(email_address)
        time.sleep(2)
        register.verify().click()

        # Connect to Gmail's IMAP server
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_address, password)
        imap.select("inbox")

        search_criteria = '(FROM "noreply@hubspot.com")'
        result, email_ids = imap.search(None, search_criteria)

        if result == "OK":
            email_id_list = email_ids[0].split()
            if email_id_list:
                # Get the first email
                first_email_id = email_id_list[0]
                result, data = imap.fetch(first_email_id, "(RFC822)")

                if result == "OK":
                    raw_email = data[0][1]
                    email_message = email.message_from_bytes(raw_email)

                    subject, encoding = decode_header(email_message["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")

                    OTP = subject[0:6]

        OTP_index = 0
        Input_index = 0
        Input = register.OTP_Input()
        while OTP_index < len(OTP):
            Input[Input_index].send_keys(OTP[OTP_index])
            Input_index += 1
            OTP_index += 1

        register.Next_button().click()

    @pytest.fixture(params=credentials.data)
    def get_credentials(self, request):
        return request.param






