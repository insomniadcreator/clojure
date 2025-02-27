
def get_location(name, city, street, house):
    """Формирует полный почтовый адрес."""
    return f"{name}, {city}, ул. {street}, д. {house}"

def get_vladivostok_address(name, street, house):
    respectful_name = f"Многоуважаемый(ая) {name}"
    return get_location(respectful_name, "Владивосток", street, house)

if __name__ == "__main__":
    address = get_vladivostok_address("Иван Иванов", "Ленина", 15)
    print(address)