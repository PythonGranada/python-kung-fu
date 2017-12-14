from operator import itemgetter
import argparse

def day_1(captcha):
    next_element_tuples = zip(captcha,(captcha*2)[1:len(captcha)+1])
    # filter the ones that are equal
    equal_elements = filter(lambda x: x[0] == x[1], next_element_tuples)
    # sum the 1st element from each tuple
    solution = sum(map(itemgetter(1), equal_elements))
    return solution

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Advent of Code 2017: day 1")
        parser.add_argument('-s', '--sequence', dest='sequence', type=str, help='Input sequence from console', required=True)

        args = parser.parse_args()

        captcha = list(map(int, args.sequence))
        

        print("Solution: {0}".format(day_1(captcha)))

    except Exception as e:
        print("Error in execution: {0}".format(str(e)))
