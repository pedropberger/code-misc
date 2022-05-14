# Print your answers to 1 decimal place within this function
    mean = sum(vals)/n
    soma = 0
    for i in range(n):
        soma = soma + (vals[i]-mean)**2
    std=(soma/n)
    std=std**(1/2)
    print(std)
