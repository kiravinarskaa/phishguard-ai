from tools.email_parser import (
    # import the parser functions that we want to test.
    extract_sender,
    extract_subject,
    extract_urls,
)

# a small fake email used as input for all tests.
sample_email = """ 
From: Security Team <security@example.com>
Subject: Password reset

Please open:
https://example.com/reset
"""


def test_extract_sender():
    assert extract_sender(sample_email) == "security@example.com"


def test_extract_subject():
    assert extract_subject(sample_email) == "Password reset"


def test_extract_urls():
    assert extract_urls(sample_email) == [
        "https://example.com/reset"
    ]