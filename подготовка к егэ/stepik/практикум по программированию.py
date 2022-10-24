countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
for i in range(len(countries)):
    cap = capitals[i]
    country = countries[i]
    popul = population[i]
    print(f'{cap} is the capital of {country}, population equal {popul} people.')
