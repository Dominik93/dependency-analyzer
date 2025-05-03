from multiprocessing import Pool


class Executor:

    def add(self, method, arguments):
        pass

    def execute(self):
        pass


class SyncExecutor(Executor):

    def __init__(self):
        self.results = []

    def add_all(self, items, method, arguments):
        """Method - first argument of this must be item in list"""
        for item in items:
            args = [item]
            args.extend(arguments)
            self.add(method, args)

    def add(self, method, arguments):
        self.results.append(method(*arguments))

    def execute(self):
        return self.results


class AsyncExecutor(Executor):

    def __init__(self):
        self.results = []
        self.pool = Pool()

    def add_all(self, items, method, arguments):
        """Method - first argument of this must be item in list"""
        for item in items:
            args = [item]
            args.extend(arguments)
            self.add(method, args)

    def add(self, method, arguments):
        self.results.append(self.pool.apply_async(method, arguments))

    def execute(self):
        for result in self.results:
            result.get()
        results = self.results
        self.pool.close()
        self.pool.join()
        return results
