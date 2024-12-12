import time

def current_sidereal_time():
    # Получаем количество секунд с начала эпохи Unix
    seconds_since_epoch = time.time()

    # Время в юлианских днях с начала эпохи
    julian_days = seconds_since_epoch / 86400 + 2440587.5
    
    # Звёздное время в часах
    sidereal_time = (280.46061837 + 360.98564736629 * (julian_days - 2451545)) % 360
    
    # Преобразуем в часы, минуты, секунды
    hours = int(sidereal_time / 15 + 3) % 24
    minutes = int((sidereal_time % 15) * 4)
    seconds = int((((sidereal_time % 15) * 4) % 1) * 60)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"