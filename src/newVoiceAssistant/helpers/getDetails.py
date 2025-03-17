def get_details():
    with open('details.txt', 'r') as file:
        details = file.readlines()
    for counter in range(len(details)):
        details[counter - 1] = details[counter - 1].replace('\n', '')
    return details
