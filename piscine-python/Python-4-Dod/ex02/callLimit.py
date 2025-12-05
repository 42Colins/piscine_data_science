def callLimit(limit: int):
    """Function to limit the number of calls to a function"""
    count = 0

    def callLimiter(function):
        """Function to limit the number of calls to a function"""
        def limit_function(*args: any, **kwds: any):
            """Function to limit the number of calls to a function"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"""Error: {function} call too many times""")
            else:
                function(*args, **kwds)
            return count
        return limit_function
    return callLimiter
