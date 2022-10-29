import people
import salary
import datetime


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    dt_now = datetime.datetime.now()
    print(dt_now)
print("Finished if __name__ == '__main__'")