# parameters of salt and paper
N = 1
P = 0.5

# salt_and_pepper
NOISE_LEVEL = 0.4def salt_and_pepper(data, noise_level=NOISE_LEVEL, n=N, p=P):
    a = np.random.binomial(size=data.shape, n=n, p=(1 - noise_level))
    b = np.random.binomial(size=data.shape, n=n, p=p)
    c = np.equal(a, 0) * b
    return data * a + c
	
 def salt_and_pepper(data, noise_level=NOISE_LEVEL, p=P):
     b, h, w, d =data.shape
     noise = np.random.choice([0, 1], size=b*h*w*d, p=[noise_level, 1-noise_level])
     noise = noise.reshape(data.shape)
     return  data * noise