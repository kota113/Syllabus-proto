import datetime

# calculate year and semester
def getYear(): str(datetime.now().year)
# 春休みの始まり(2月)から春学期の終わり(7月)まではspring、それ以外はfall
def getSemester(): "spring" if 2 <= datetime.now().month <= 7 else "fall"