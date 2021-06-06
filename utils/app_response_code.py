from enum import Enum


class ResponseCode(Enum):
    SUCCESS = "90000"
    UNKNOWN = "AX10001"
    MISSING_FIELD = "AX10002"
    VALIDATION_FAILED = "AX10003"
