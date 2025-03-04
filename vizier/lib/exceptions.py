class GenericError(Exception):

    """Base class for generic errors"""

    pass


class ValidationError(GenericError):

    """Base class for validation errors"""

    pass


class OperationError(GenericError):

    """Base class for operation errors"""

    pass


class APIError(GenericError):

    """Base class for API errors"""

    pass


class MissingValueError(ValidationError):

    """Exception raised when a needed value is None"""

    def __init__(self, message="Missing value"):
        super().__init__(message)


class DatabaseError(OperationError):

    """Exception raised when a database operation fails"""

    def __init__(self, message="Database error"):
        super().__init__(message)


class FileError(OperationError):

    """Exception raised when a file operation fails"""

    def __init__(self, message="File error"):
        super().__init__(message)


class APITimeoutError(APIError):

    """Exception raised when an API call times out"""

    def __init__(self, message="API timed out"):
        super().__init__(message)


class APIConnectionError(APIError):

    """Exception raised when an API fails to stablish connection"""

    def __init__(self, message="API connection error"):
        super().__init__(message)

        
class APINonRetriableError(APIError):

    """Exception raised when a non-retriable error occurs"""

    def __init__(self, message="API non retriable error"):
        super().__init__(message)