if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    no_passenger = data['passenger_count'] != 0
    zero_trip = data['trip_distance'] != 0

    data = data[no_passenger & zero_trip]
    data['lpep_pickup_date'] = data.lpep_pickup_datetime.dt.date

    print(data['VendorID'].unique())
    print(len(data['lpep_pickup_date'].unique()))

    data.rename(columns=lambda x: x.lower(), inplace=True)

    return data[no_passenger & zero_trip]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
