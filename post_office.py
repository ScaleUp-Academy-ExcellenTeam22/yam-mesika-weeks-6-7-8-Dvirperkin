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

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
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
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False  # Indicates if the message read or not.
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

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
            if not mail["read"]:
                unread_first_n_mails.append(mail)
                mail["read"] = True
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
        return [mail for mail in user_box if str_to_contain in mail["body"]]


if __name__ == '__main__':
    """Show example of using the PostOffice class."""
    users = ['Newman', 'Mr. Peanutbutter']
    post_office = PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Dvir.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Dvir.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Dvir.',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Newman'])

    print(post_office.read_inbox("Newman", 9))
    print(post_office.read_inbox("Newman", 9))
    print(post_office.search_inbox("Newman", "Dvir"))
