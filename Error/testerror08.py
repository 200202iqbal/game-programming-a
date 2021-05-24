def func():
    raise IOError
try:
    func()
except IOError as exc:
    raise RuntimeError("Failed to open database") c