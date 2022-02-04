from wrappers.covid_api import CovidApi

covid_resolver = CovidApi()

worldwide_summary = CovidApi().worldwide_summary()

print(worldwide_summary)

