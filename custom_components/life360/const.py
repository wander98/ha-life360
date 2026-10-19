"""Constants for Life360 integration."""

from aiohttp import ClientTimeout

DOMAIN = "life360"

ATTRIBUTION = "Data provided by life360.com"
COMM_MAX_RETRIES = 4
COMM_TIMEOUT = ClientTimeout(sock_connect=15, total=60)
LOGIN_ERROR_RETRY_DELAY = 5 * 60
LTD_LOGIN_ERROR_RETRY_DELAY = 60
MAX_LTD_LOGIN_ERROR_RETRIES = 30
SPEED_FACTOR_MPH = 2.25
SPEED_DIGITS = 1
DEFAULT_UPDATE_INTERVAL = 15
MIN_UPDATE_INTERVAL = 5
MAX_UPDATE_INTERVAL = 600
# Rate limits shorter than this are retried quietly and do not change account status.
RATE_LIMIT_STATUS_THRESHOLD = 60

ATTR_ADDRESS = "address"
ATTR_AT_LOC_SINCE = "at_loc_since"
ATTR_DRIVING = "driving"
ATTR_LAST_SEEN = "last_seen"
ATTR_PLACE = "place"
ATTR_REASON = "reason"
ATTR_SPEED = "speed"
ATTR_WIFI_ON = "wifi_on"
ATTR_IGNORED_UPDATE_REASONS = "ignored_update_reasons"
ATTR_ACCOUNT_STATUS = "account_status"
ATTR_LAST_ERROR = "last_error"
ATTR_LAST_SUCCESS = "last_success"
ATTR_RATE_LIMITED_UNTIL = "rate_limited_until"
ATTR_UPDATE_INTERVAL = "update_interval"

STATE_DRIVING = "driving"

STATUS_LOGIN_ERROR = "login_error"
STATUS_OFFLINE = "offline"
STATUS_ONLINE = "online"
STATUS_RATE_LIMITED = "rate_limited"

CONF_ACCOUNTS = "accounts"
CONF_AUTHORIZATION = "authorization"
CONF_DRIVING_SPEED = "driving_speed"
CONF_MAX_GPS_ACCURACY = "max_gps_accuracy"
CONF_SHOW_DRIVING = "driving"
CONF_TOKEN_TYPE = "token_type"
CONF_UPDATE_INTERVAL = "update_interval"
CONF_VERBOSITY = "verbosity"

SERVICE_UPDATE_LOCATION = "update_location"

SIGNAL_ACCT_STATUS = "life360_acct_status"
SIGNAL_MEMBERS_CHANGED = "life360_members_changed"
SIGNAL_UPDATE_LOCATION = "life360_update_location"
