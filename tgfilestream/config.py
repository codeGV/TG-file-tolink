
import sys
import os

from yarl import URL

try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = os.environ.get("TG_API_ID")
    api_hash = os.environ.get("TG_API_HASH")
except (KeyError, ValueError):
    print("Please set the TG_API_ID and TG_API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

trust_headers = bool(os.environ.get("TRUST_FORWARD_HEADERS"))
host = os.environ.get("HOST", "localhost")
public_url = URL(os.environ.get("PUBLIC_URL", ""))

session_name = os.environ.get("TG_SESSION_NAME", "")

log_config = os.environ.get("LOG_CONFIG")
debug = bool(os.environ.get("DEBUG"))

try:
    # The per-user ongoing request limit
    request_limit = int(os.environ.get("REQUEST_LIMIT", "5"))
except ValueError:
    print("Please make sure the REQUEST_LIMIT environment variable is an integer")
    sys.exit(1)

try:
    # The per-DC connection limit
    connection_limit = int(os.environ.get("CONNECTION_LIMIT", "20"))
except ValueError:
    print("Please make sure the CONNECTION_LIMIT environment variable is an integer")
    sys.exit(1)


start_message = os.environ.get("TG_START_MESG", "Send an image or file to get a link to download it")
group_chat_message = os.environ.get("TG_G_C_MESG", "Sorry. But, I only work in private.")
