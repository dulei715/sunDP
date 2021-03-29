import basis.local_differential_privacy_library as ldpl
import numpy as np

if __name__ == '__main__':
    value = 5
    values = [3,4,5,6,7,8]
    epsilon = 0.1
    result = ldpl.k_random_response_new(3,4,epsilon)
    print(result)

    temp = np.array([1,2,3])
    print(type(temp))
    temp2 = temp == 1
    result = np.where(temp == 1, np.random.binomial(1, 2/3, len(temp)), np.random.binomial(1, 1/3, len(temp)))
    print(result)