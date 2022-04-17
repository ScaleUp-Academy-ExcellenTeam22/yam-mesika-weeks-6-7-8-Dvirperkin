class Message:
    """A Message class. Allows creating and read message.

        Parameters
        ----------
        identifier : int
            The identifier of the message.
        sender : str
            The message sender's name.
        title : str
            The title of the message.
        body : str
            The body of the message.

        Attributes
        ----------
        id : int
            The identifier of the message
        sender : str
            The message sender's name.
        title : str
            The title of the message
        body : str
            The body of the message.
        size : int
            The size of the body of the message.
        read : bool
            Indicates if the message has been read.
        """
    def __init__(self, identifier, sender, title, body):
        self.id = identifier
        self.sender = sender
        self.title = title
        self.body = body
        self.size = len(body)
        self.read = False

    def is_read(self):
        return self.read

    def read_msg(self):
        self.read = True
        return "Message title: " + self.title + " Message body: " + self.body

    def contain(self, string_to_check):
        """
        :param string_to_check: The requested string to check if the message contain it.
        :return: True if the message contain the given string else False.
        """
        return string_to_check in self.body or string_to_check in self.title

    def __str__(self):
        return "Message title: " + self.title + "\n" + "Message body: " + self.body

    def __len__(self):
        return len(self.body)
