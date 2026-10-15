# import the function that extracts structured information from an email.
from tools.email_parser import parse_email


def main():
    # open sample email in read mode.
    # "with" automatically closes the file when reading is finished
    with open(
        "samples/sample_email.txt",
        "r",
        encoding="utf-8"
    ) as file:
        # read the whole email and store it as one string
        email_text = file.read()

    # send the email text to our parser.
    # the returned dictionary contains sender, subject, and URLs.
    result = parse_email(email_text)

    print(result)  # display the parser result for now.
    # later, this data will be passed to the AI agent.


# run main() only when this file is executed directly.
# do not run it automatically if main.py is imported by another file.
if __name__ == "__main__":
    main()