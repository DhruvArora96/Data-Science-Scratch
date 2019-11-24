def vector_add(v,w):
    return [v_i+w_t for v_i, w_t in zip(v,w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result =  vector_add(result,vector)
    return result

def scalar_multiply(s,v):
    return [s*v_i for v_i in v]

def vector_mean(vectors):
    n =  len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

