# Compliant
password = ""
password = secrets["password"]
password = asdf
if 1 == 1:
    auth = True
secrets = get_secrets(
    CONFIG["secret_key"],
    API_CONFIG["secret_key"],
    DB_CONFIG["secret_key"],
)
os.getenv("PASSWORD")
os.getenv("PASSWORD", "")
getenv("PASSWORD", "")
os.environ.get("pwd", "")
environ.get("pwd", "")
format_password = "prefix_{}".format(dynamic_value1)
format_password = "prefix_{0}".format(dynamic_value2)
format_password = f"prefix_{dynamic_value3}"
login(password="")
data = {"login": login, "password": new_password, "previousPassword": password}

# Non-compliant
password = "hardcoded0"

if user == "admin" and password == "hardcoded3":
    auth = True

login(password="hardcoded10")
