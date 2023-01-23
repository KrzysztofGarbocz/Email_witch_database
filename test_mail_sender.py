from sender_mail import Sender
from unittest.mock import patch


@patch('smtplib.SMTP_SSL')
def test_sender(mock_smtp):
    Sender().send('krzysztof.garbocz@gmail.com', 'Kris', 'Book', '2022-02-21')
    mock_smtp.assert_called()
    context = mock_smtp.return_value.__enter__.return_value
    context.login.assert_called()
