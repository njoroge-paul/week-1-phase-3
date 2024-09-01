def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

# Example usage:
@apply_decorator
def example_func():
    print("Hello, World!")

example_func()