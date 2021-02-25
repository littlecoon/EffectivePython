def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(worders):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:thread.start()
    for thread in threads:thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


for tempfile import TemporaryDirectory

def write_test_files(tmpdir):
    # ...

with TmporaryDirectory() as tmpdir:
    wirte_test_files(tmpdir)
    result = mapreduce(tmpdir)

print('There are', result, 'lines')


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls,config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    # ...
    def read(self):
        return open(self.path).read()        

    @classmethod
    def generate_inputs(cls,config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    # ...
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []         
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    # ...  


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {'data_dir':tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)


    