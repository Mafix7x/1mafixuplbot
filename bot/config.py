import os


class Config:

    BOT_TOKEN = "1117107660:AAExjFFYdxl8kSTn-9nHWGVFQ5R5TnonmaQ"
    SESSION_NAME = ":memory:"

    API_ID = "26489380"

    API_HASH = "4167d8b8779aab33b73810feb3c77021"

    CLIENT_ID = "642978573000-02vrq5kussq9t1h65r1sff2f5o03gjls.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "932420516"

    AUTH_USERS_TEXT = "932420516"

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
