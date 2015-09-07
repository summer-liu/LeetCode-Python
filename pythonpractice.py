# from functools import reduce
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisible(n):
# 	print('n:',n)
# 	return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列    

# # 打印1000以内的素数:
# for n in primes():
#     if n < 10:
#         print(n)
#     else:
#         break        



def log(func):
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw)
	return wrapper
# @log
def now():
	print('hill')


now = log(now)
now()