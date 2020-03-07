import sv_data_processor
from collections import namedtuple


def main():
    # name	id	nametype	recclass	mass (g)	fall	year	reclat	reclong	GeoLocation
    opened_file = sv_data_processor.open_seperated_value_file(
        "datasets/mystery_data.tsv"
    )
    Meteor = namedtuple("Meteor", next(opened_file))
    piped_values = sv_data_processor.pipe_seperated_values(
        [[str, int, str, str, int, str, str, float, float, str]], opened_file
    )
    meteorites = map(lambda data: sv_data_processor.apply_namedtuple(Meteor, data), piped_values)


main()
