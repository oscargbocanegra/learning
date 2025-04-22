def get_population():
    keys = ['col', 'bol', 'ven', 'per', 'par', 'uru', 'bra', 'chi', 'ecu', 'guy']
    values = [50_000_000, 12_000_000, 30_000_000, 35_000_000, 7_000_000, 3_500_000, 210_000_000, 1_500_000, 17_000_000, 1_200_000]
    return keys, values

def population_by_country(data, country):
    """
    Function to get the population of a country.
    :param data: Tuple with keys and values
    :param country: Country to get the population
    :return: Population of the country
    """

    result = list(filter(lambda item: item['Country'] == country, data))
    return result
