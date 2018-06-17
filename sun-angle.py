# Your task is to find the angle of the sun above the horizon knowing the
# time of the day. Input data: the sun rises in the East at 6:00 AM, which
# corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith,
# which means that the angle equals 90 degrees. 6:00 PM is the time of the
# sunset so the angle is 180 degrees. If the input will be the time of the night
# (before 6:00 AM or after 6:00 PM), your function should return
# - "I don't see the sun!".

# Input: The time of the day
# Output: the angle of the sun, rounded to 2 decimal places

def sun_angle(time):
    hours = int(time[:2])
    # print(hours)
    minutes = int(time[3:])
    # print(minutes)
    result = 0
    if hours > 6 and hours < 18:
        result = (hours-6) * 15 + (minutes * 0.25)
    else:
        return "I don't see the sun!"
    return result


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
