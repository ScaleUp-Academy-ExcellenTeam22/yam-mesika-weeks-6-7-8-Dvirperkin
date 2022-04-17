from message import Message


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        title : str
            The title of the message
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1

        msg = Message(self.message_id, sender, title, message_body)

        if urgent:
            user_box.insert(0, msg)
        else:
            user_box.append(msg)
        return msg.id

    def read_inbox(self, username, N):
        """
        Reads the first n unread mail in the user mailbox.
        :param username: The identifier of the username.
        :param N: The number of mail to read.
        :raise KeyError If the recipient does not exist.
        :return: A list containing at most N unread mails.
        """
        user_box = self.boxes[username]

        if N > len(user_box):
            N = len(user_box)

        unread_first_n_mails = []
        for mail in user_box:
            if not mail.is_read():
                unread_first_n_mails.append(mail.read_msg())
                N -= 1
            if not N:
                break
        return unread_first_n_mails

    def search_inbox(self, username, str_to_contain):
        """
        :param username: The identifier of the username.
        :param str_to_contain: The requested string to be included in the mails.
        :raise KeyError If the recipient does not exist.
        :return: A list containing all the mails that containing the given string.
        """
        user_box = self.boxes[username]
        return [mail.read_msg() for mail in user_box if mail.contain(str_to_contain)]


if __name__ == '__main__':
    """Show example of using the PostOffice class."""
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Dvir.',
        message_body='bye, Dvir.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Dvir.',
        message_body='bye, Dvir.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Newman.',
        message_body='bye, Newman.',
    )
    post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        title='Hello, Dvir.',
        message_body='bye, Dvir.',
    )

    print(post_office.read_inbox("Newman", 9))
    print(post_office.read_inbox("Newman", 9))
    print(post_office.search_inbox("Newman", "Dvir"))
