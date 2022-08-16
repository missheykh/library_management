from pathlib import Path


BASE_DIR=Path(__file__).resolve().parent
# print(BASE_DIR)

USER_DATA_PATH= BASE_DIR/"users_data"
# print(USER_DATA_PATH)

BOOKS_DATA_PATH=BASE_DIR/"books_data"
# print(BOOKS_DATA_PATH)