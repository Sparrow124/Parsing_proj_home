from bs4 import BeautifulSoup
import threading
import requests
import time

from firstapp.models import DataBeforeParsing, DataAfterParsing


def get_timeshift_url():  # here we get bundle url+shift for sorting by timer and adding to dictionary
    dict_with_url_timeshift = {}
    main_data = DataBeforeParsing.objects.all()
    for i in main_data:
        a = i.site_url
        b = i.seconds_shift+(60*i.minutes_shift)+(3600*i.hours_shift)
        z = {a: b}
        dict_with_url_timeshift.update(z)
    new_dict = sorted(dict_with_url_timeshift.items(), key=lambda kv: kv[1])
    return new_dict


def sleepy(value):  # function for sleep in threads
    return time.sleep(value)


def parsing_url(request):  # doing parsing based on timeshift and adding result to db
    dict_value = get_timeshift_url()
    threads = []
    for key, value in dict_value:
        values = [value]
        t = threading.Thread(target=sleepy, args=values)
        t.start()
        threads.append(t)

        for thread in threads:
            thread.join()

        try:
            html_content = requests.get(key)
            status = html_content.status_code
            print(key, 'SUCCESS:', status)  # success or error information
        except requests.exceptions.RequestException:  # exception for connection error
            DataAfterParsing.objects.create(site_connect=status, site_url=key)
            print('STATUS FAILED:', status)
        else:
            if status == 200:
                list_with_parsdata = []
                soup = BeautifulSoup(html_content.content, 'html.parser')
                try:  # doing exception to each field what we need, cuz if return None we will get error
                    list_with_parsdata.append(str(soup.title.string))
                except AttributeError:
                    list_with_parsdata.append(str(soup.title))
                except Exception:
                    list_with_parsdata.append(None)

                try:
                    list_with_parsdata.append(str(soup.h1.string))
                except AttributeError:
                    list_with_parsdata.append(str(soup.h1))
                except Exception:
                    list_with_parsdata.append(None)

                try:
                    list_with_parsdata.append(str(soup.original_encoding))
                except AttributeError:
                    list_with_parsdata.append(None)

                DataAfterParsing.objects.create(site_connect=status, site_url=key, site_title=list_with_parsdata[0],\
                                                main_heading=list_with_parsdata[1], content_type=list_with_parsdata[2])
