'''
provided by kasaiee
Email : 1tapciran@gmail.com
https://ir.linkedin.com/in/kasaiee
'''
def power(base, exponent):
    if exponent % 1 != 0:
        return base ** 1. / exponent
    else:
        res=1
        catch_base = base
        def calc():
            yield catch_base * res
        for item in range(exponent):
            res =  calc().next()
        return res

if __name__ == '__main__':
	base = input('insert base: ')
	exponent = input('insert exponent: ')
	print power(base, exponent)
