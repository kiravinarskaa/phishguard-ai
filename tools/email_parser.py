import re # for regular expressions


def extract_sender(email_text):
    """
    Extract the sender email address from the From field.

    Example:
    From: Microsoft Security <security@example.com>

    Returns:
    security@example.com
    """

    # check the email line by line to find the "From:" header
    for line in email_text.splitlines():
        # convert the line to lowercase only for comparison,
        # so "From:", "FROM:", and "from:" are all accepted.
        if line.lower().startswith("from:"):
            # remove "From:" and any extra spaces around the remaining text.
            sender_line = line[5:].strip()

        # first try to find an email address inside angle brackets:
            # Like: Microsoft Security <security@example.com>
            match = re.search(r"<([^<>]+@[^<>]+)>", sender_line)

            if match:
                return match.group(1)
            # group(1) returns only the content inside the parentheses
            # in the regular expression.

            email_match = re.search(
                 # If there are no angle brackets, try to find
                  # a normal email address directly in the From line.
                r"[\w.\-+]+@[\w.\-]+\.\w+",
                sender_line
            )

            if email_match:
                return email_match.group(0)

    return None  # return None if no sender address was found.


def extract_subject(email_text):
    """
    Extract the Subject field from the email.
    """

    for line in email_text.splitlines():
        if line.lower().startswith("subject:"):
            return line[8:].strip()

    return None


def extract_urls(email_text):
    """
    Extract HTTP and HTTPS URLs from the entire email.
    """

    # regex pattern that matches links beginning with
    # http:// or https:// and continues until whitespace
    # or certain special characters.
    url_pattern = r"https?://[^\s<>\"']+"

    # Find every URL in the email.
    # findall() returns a list.
    urls = re.findall(url_pattern, email_text)

    return urls


def parse_email(email_text):
    """
    Run all parser functions and return the results
    in one structured dictionary.
    """

    return {
    # combine the extracted data into one dictionary.
    # later, Agent 1 can use these values directly.
        "sender": extract_sender(email_text),
        "subject": extract_subject(email_text),
        "urls": extract_urls(email_text),
    }