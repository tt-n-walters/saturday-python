from os.path import isfile

accepted_filetypes = {
    "csv": ",",
    "tsv": "\t"
}

def open_seperated_value_file(filename):
    if not isfile(filename):
        raise FileNotFoundError
    filetype = filename.rpartition(".")[2]
    if not filetype in accepted_filetypes:
        raise NotImplementedError
    try:
        file = open(filename, "r", encoding="utf-8")
    except:
        file = open(filename, "r")
    finally:
        yield next(file)
        for line in file:
            yield line.strip().split(accepted_filetypes[filetype])


def pipe_seperated_values(pipeline, values):
    for pipe in pipeline:
        for processor, item in zip(pipe, next(values)):
            yield processor(item)


def apply_namedtuple(named_tuple, data):
    return named_tuple(*data)


if __name__ == "__main__":
    opened_file = open_seperated_value_file("datasets/data_person_1000000.csv")

    from collections import namedtuple
    from pprint import pprint
    Person = namedtuple("Person", next(opened_file))
    
    piped_values = pipe_seperated_values([[
        str,
        str,
        float,
        int,
        str
    ]], opened_file)
    
    map(lambda data: apply_namedtuple(Person, data), piped_values)