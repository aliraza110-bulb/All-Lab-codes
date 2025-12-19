encrypted_id="USR-2025-11-PAK-98342-XY"

year=encrypted_id[4:8]

country=encrypted_id[12:15]

serial=encrypted_id[16:21]

month=encrypted_id[10:11]

region=encrypted_id[0:2]

random_suffix=encrypted_id[22:24]

print("year",year)
print("country",country)
print('Serial',serial)
print("Month",month)
print("Region",region)
print("Random Suffix",random_suffix)

if encrypted_id[4:8] == ("2025") and encrypted_id[4:8] > ("2020"):
    print("The Id Is Validate ",encrypted_id[4:8])
else:
    print("Id Is Not Valid",encrypted_id[4:8])

