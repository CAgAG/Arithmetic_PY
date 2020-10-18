import math

if __name__ == '__main__':
    x, y = 1, 2

    math.gcd(x, y)  # gcd:返回x和y的最大公约数

    math.modf(x)  # 返回x的小数和整数
    math.fsum([x, y, ...])  # 返回无损精度的和
    math.factorial(x)  # 返回x的阶乘
    math.isinf(x)  # 若x为正无穷大或负无穷大，返回True；否则，返回False
    math.isfinite(x)  # 如果x是正无穷大或负无穷大，则返回True, 否则返回False


    #  math.e     自然常数e     
    #  math.pi     圆周率pi     
    #  math.degrees(x)     弧度转度     
    #  math.radians(x)     度转弧度     
    #  math.exp(x)     返回e的x次方     
    #  math.expm1(x)     返回e的x次方减1     
    #  math.log(x[, base])     返回x的以base为底的对数，base默认为e     
    #  math.log10(x)     返回x的以10为底的对数     
    #  math.log1p(x)     返回1 + x的自然对数（以e为底）
    #  math.pow(x, y)     返回x的y次方 == pow
    #  math.sqrt(x)     返回x的平方根     
    #  math.ceil(x)     返回不小于x的整数
    #  math.floor(x)     返回不大于x的整数
    #  math.trunc(x)     返回x的整数部分     
    #  math.fabs(x)     返回x的绝对值     
    #  math.fmod(x, y)     返回x % y（取余）     
    #  math.isnan(x)     若x不是数字，返回True；否则，返回False
    #  math.copysign(x, y)     若y < 0，返回 -abs(x)；否则，返回x的绝对值
    #  math.frexp(x)     返回m和i，满足m乘以2的i次方     
    #  math.ldexp(m, i)     返回m乘以2的i次方     
    #  math.hypot(x, y)   返回以x和y为直角边的斜边长 -> x^2+y^2 
    #  math.sin(x)     返回x（弧度）的三角正弦值     
    #  math.asin(x)     返回x的反三角正弦值     
    #  math.cos(x)     返回x（弧度）的三角余弦值     
    #  math.acos(x)     返回x的反三角余弦值     
    #  math.tan(x)     返回x（弧度）的三角正切值     
    #  math.atan(x)     返回x的反三角正切值     
    #  math.atan2(x, y)     返回x / y的反三角正切值     
    #  math.sinh(x)     返回x的双曲正弦函数     
    #  math.asinh(x)     返回x的反双曲正弦函数     
    #  math.cosh(x)     返回x的双曲余弦函数     
    #  math.acosh(x)     返回x的反双曲余弦函数     
    #  math.tanh(x)     返回x的双曲正切函数     
    #  math.atanh(x)     返回x的反双曲正切函数     
    #  math.erf(x)     返回x的误差函数     
    #  math.erfc(x)     返回x的余误差函数     
    #  math.gamma(x)     返回x的伽玛函数     
    #  math.lgamma(x)     返回x的绝对值的自然对数的伽玛函数
