import random

print("\n")

print("3 ile 20 arasında rastgele bir sayı >>>>> ", random.randint(3, 20))

print("Düzgün dağılımlı, 20 ile 60 arasında bir sayı >>>>> ", random.uniform(20, 60))


print("Ortlaması 5, standradr sapması 4 olan normal dağılımlı bir sayı >>>>> ", random.normalvariate(mu = 5, sigma = 4))

print("Daha birçok rastgele sayı oluşturabileceğiniz bir modül.")
print("Ayrıntılar https://docs.python.org/3/library/random.html")