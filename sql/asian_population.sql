'''
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:
https://www.hackerrank.com/challenges/asian-population/problem
'''

select sum(city.population) from city join COUNTRY on city.countrycode = country.code where country.continent ='Asia';
