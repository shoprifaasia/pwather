import json
import argparse
import requests

def setup_parser(arguments, title):
        parser = argparse.ArgumentParser(description=title,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        for key, val in arguments.items():
                parser.add_argument('-%s' % key,
                            default=arguments[key] )
                for k , v in val.items():
                    if type(v) == 'dict':
                        parser.add_argument('-%s' % k,
                            default=val[k])
        return parser


def read_params(parser):
    parameters = vars(parser.parse_args())
    return parameters

def get_parameters(title=None):

    with open("location.json") as data_file:
        data = json.loads(data_file)
    # print data
    parser = setup_parser(data, title)
    parameters = read_params(parser)

    return parameters

if __name__ == "__main__":
        url = 'http://api.weatherapi.com/v1/current.json?key=ca906cb4997343508e7165953202010&q=Israel'
        r = requests.get(url)
        data = json.dumps(r.json())
        # by normal input
        print("get wather by Enter:")
        print("1- name county")
        print("2- date (yyyy-mm-dd)")
        print("Enter 0 to exit")
        name_county = input()
        while name_county != 0:
                data = json.loads(data)
                print type(data)
                if name_county == 1:
                    print("Enter name of country-israel :")
                    county = "Israel"
                    print county
                    if data["location"]["name"] == county:
                            print("temputure is : ",data["current"]["temp_c"])
                elif name_county == 2 :
                    county = "2020-10-22"
                    print data["location"]["localtime"][:10]
                    if data["location"]["localtime"][:10] == county:
                                print(data["current"]["temp_c"])
                print("get wather by Enter:")
                print("1- name county")
                print("2- date (yyyy-mm-dd)")
                print("Enter 0 to exit:")
                name_county = input()

        #second way by argsparser
        # with open('location.json','w') as file_wather:
        #         file_wather.write(data)
        # params = get_parameters()
        # print(params)