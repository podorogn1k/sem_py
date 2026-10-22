from contextlib import contextmanager

@contextmanager
def log_operation(file, operation):
    with open(file, 'a') as f:
        f.write(f"START: {operation}\n")
    try:
        yield
    except Exception:
        with open(file, 'a') as f:
            f.write(f"ERROR: {operation}\n")
    else:
        with open(file, 'a') as f:
            f.write(f"END: {operation}\n")

with log_operation("operation.log", "Data processing"):
    print("START")
    x = 10
    print("END")