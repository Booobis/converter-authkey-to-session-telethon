from telethon import TelegramBareClient


api_id = 1 # ваш api_id

api_hash = "qwerty123456789" # ваш api_hash

client = Client(":memory:", api_id, api_hash)

session_string = client.export_session_string()

auth_key = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6" # купленный / найденный auth_key

auth_key_bytes = bytes.fromhex(auth_key)

dc_id = "2" # купленный / найденный dc_id

dc_id_int = int(dc_id)

string_session = TelegramBareClient.session_string(auth_key_bytes, dc_id_int)


print(string_session)
