import doctest
import re

# Regular Expression:
# Valid email formats: https://help.xmatters.com/ondemand/trial/valid_email_format.htm
regex = r'([A-Za-z0-9]+[--_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


def check_email(email) -> bool:
    '''
    This method checks a given email address for matching the email format regex.

    if the format of the given address is valid - returns True,
    else - returns False

    TESTS:

    >>> check_email('a@mail.com')
    True
    >>> check_email('a@mail.org')
    True
    >>> check_email('a@mail.net')
    True
    >>> check_email('@mail.com')
    False
    >>> check_email('mail.com')
    False
    >>> check_email('a@mail')
    False
    >>> check_email('a')
    False

    >>> check_email('abc-@mail.com')
    False
    >>> check_email('abc-d@mail.com')
    True

    >>> check_email('abc..def@mail.com')
    False
    >>> check_email('abc.def@mail..com')
    False
    >>> check_email('.abc@mail.com')
    False
    >>> check_email('abc.def.hij@mail.com')
    True

    >>> check_email('abc.def@mail.c')
    False
    >>> check_email('abc.def@mail.cc')
    True

    >>> check_email('abc.def@mail#archive.com')
    False
    >>> check_email('abc#def@mail-archive.com')
    False
    >>> check_email('abc.def@mail-archive.com')
    True
    '''
    return True if re.fullmatch(regex, email) else False


def list_emails(file_path) -> None:
    '''
    This function gets a path to a text-file which contains email addresses, line by line ('\n' separator).
    It uses check_email's logic to create 2 seprate lists:
        1. Valid - All valid email addresses in the given file.
        2. Invalid - Other email addresses that do not match the format.

    After creating these 2 lists, the function prints them separately.

    TESTS:

    >>> list_emails('emails.txt')
    Valid Emails: ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    Invalid Emails: ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
    '''
    valid = []
    invalid = []
    with open(file_path, 'r') as f:  # Open for read only
        text = f.read()  # reading bytes of text to string.

        # extracting all email-like patterns within the text
        emails = re.findall('[\S]+@[\S]+', text)
        for email in emails:
            valid.append(email) if check_email(
                email) else invalid.append(email)  # Shorten if - filling the lists
    print(f'Valid Emails: {valid}')
    print(f'Invalid Emails: {invalid}')


if __name__ == '__main__':
    doctest.testmod()
