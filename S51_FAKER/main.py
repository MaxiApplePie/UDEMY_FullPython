from faker import Faker

faking = Faker(locale='fr_FR')

print(faking.name())

numbers = [faking.unique.random_int() for _ in range(500)]
assert len(numbers) == len(set(numbers))

