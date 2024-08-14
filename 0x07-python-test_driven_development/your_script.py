try:
    # Code that might cause an OverflowError
    result = some_large_calculation()
except OverflowError:
    print("An overflow occurred")
    result = float('inf')  # or some other appropriate fallback

