duration = int(input('Enter duration in seconds: '))
days = duration // 86400
if days > 0:
    duration %=  86400
hours = duration // 3600
if hours > 0:
    duration %= 3600
minutes = duration // 60
if minutes > 0:
    duration %= 60
seconds = duration % 60
result = ''
if days > 0:
    result = str(days) + ' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек'
elif hours > 0:
    result = str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек'
elif minutes > 0:
    result = str(minutes) + ' мин ' + str(seconds) + ' сек'
elif seconds >= 0:
    result = str(seconds) + ' сек'
print(result)