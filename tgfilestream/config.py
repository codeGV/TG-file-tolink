
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
    api_id = "13268517"
    api_hash = "d64dd905a0133fe2b15bad493b5ad274"
except (KeyError, ValueError):
    print("Please set the TG_API_ID and TG_API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

trust_headers = bool(os.environ.get("TRUST_FORWARD_HEADERS"))
host = os.environ.get("HOST", "15.207.14.92/file")
public_url = URL(os.environ.get("PUBLIC_URL", f"http://{host}:{port}"))

session_name = os.environ.get("TG_SESSION_NAME", "1BVtsOJwBu3X9W_FdwLUoi5NJCShhbgvOFI8k9dTejVVCsF6hto5UmbmE-PlH66sXcM4WMYlMELMDp9bxpm4uz0dPDrewIUy1sK8grOQSrgvMKmNf3a2OX2_iIccr04TYQH4fvskxPog43-o_0QaAuH0Km8yMLWB5oQv_bf3IqLL86Mpp3t6ak6X5ZfDgX4V4nDY_D5SC935WezSEWU1HzbtnctAezT911pSNFdpaCaLPgUdCZdJMMTXr9F7kfXAW7eroxIc57J9UCqQsaxfItv9pTeQbWRSy3rX8lJgHRYIX8Tw-4pA6_mt_5qVlo7II4kJowJtiKSAHYPsq4dXnjXwu9dlAbWI=")

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
