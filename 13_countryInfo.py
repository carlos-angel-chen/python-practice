from countryinfo import CountryInfo

country = input("Enter a contry name: ")
countryInfo = CountryInfo(country)

print(countryInfo.capital())
print(countryInfo.currencies())
print(countryInfo.flag())
