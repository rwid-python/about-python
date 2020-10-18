# Introducing Dictionary Data Type like as JSON
# Dictionary like as array but but use {} and can combine with array.
# KVP : Key Value Pair

# Example Dictionary --> Translator
# 1st
kamus_en_id = {}
kamus_en_id['mother'] = 'ibu'
kamus_en_id['father'] = 'ayah'
kamus_en_id['son'] = 'mas'
print(kamus_en_id)
i = 'mother'
print(f"Translate EN to ID word {i} : {kamus_en_id[i]}")
# 2nd
kamus_en_id = {'mother': 'ibu', 'father': 'ayah', 'son': 'mas'}
print(kamus_en_id)
i = 'father'
print(f"Translate EN to ID word {i} : {kamus_en_id[i]}")

# Example Expert Data Dictionary as Gojek
data_driver = {'date': '2020-10-10',
               'driver': [
                   {'name': 'eko', 'jarak': 100},
                   {'name': 'dwi', 'jarak': 200},
                   {'name': 'tri', 'jarak': 300},
                   {'name': 'catur', 'jarak': 400},
                   {'name': 'ponco', 'jarak': 500}
               ]}
print(f"Driver #1 {data_driver['driver'][0]}")
print(f"Who is The Driver sort {data_driver['driver'][0]['jarak']} meter")
