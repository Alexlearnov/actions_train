import traceback

try:
    # Некоторый код
    open("non_existent_file.txt")
except Exception as e:
    error_details = traceback.format_exc()
    with open("error.log", "a") as log_file:
        log_file.write(error_details)
    print("Произошла ошибка. Пожалуйста, свяжитесь с поддержкой.")
