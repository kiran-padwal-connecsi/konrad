import datetime
import requests
from connecsiApp import base_url


class Campaign:
    def __init__(self,user_id,campaign_id=''):
        self.user_id=user_id
        self.campaign_id=campaign_id
        self.url_view_campaigns = base_url + 'Campaign/' + str(self.user_id)
        self.url_view_campaign_details = base_url + 'Campaign/' + str(self.campaign_id) + '/' + str(self.user_id)
        self.url_getYoutubeInfList = base_url + 'Brand/getYoutubeInfList/'
        self.url_update_campaign_status = base_url + 'Campaign/update_campaign_status/'

    def get_all_campaigns(self):
        view_campaign_data = ''
        try:
            view_campaigns_response = requests.get(url=self.url_view_campaigns)
            view_campaign_data = view_campaigns_response.json()
            print('test', view_campaign_data)
            for item in view_campaign_data['data']:
                # print(item)
                region_id_list = item['regions'].split(',')
                region_name_list = []
                for region_id in region_id_list:
                    try:
                        region_name_response = requests.get(url=base_url + 'Youtube/regionCode/' + str(region_id))
                        region_data = region_name_response.json()
                        region_name = region_data['data'][0][1]
                        region_name_list.append(region_name)
                    except:
                        pass
                cat_response = requests.get(url=base_url + 'Youtube/videoCategories/' + str(item['video_cat_id']))

                cat_json_data = cat_response.json()
                video_cat_name = cat_json_data['data'][0]['video_cat_name']
                item.update({'video_cat_name': video_cat_name})
                item.update({'region_name_list': region_name_list})
                try:
                    string_from_date = datetime.datetime.strptime(item['from_date'], '%Y-%m-%d')
                    string_from_date = string_from_date.strftime('%d-%b-%y')
                    string_to_date = datetime.datetime.strptime(item['to_date'], '%Y-%m-%d')
                    string_to_date = string_to_date.strftime('%d-%b-%y')
                    item.update({'from_date': string_from_date})
                    item.update({'to_date': string_to_date})
                except Exception as e:
                    print(e)
                try:
                    youtubeInfListResponse = requests.get(url=self.url_getYoutubeInfList+str(item['campaign_id']))
                    youtubeInfList_data = youtubeInfListResponse.json()
                    no_of_youtube_influencers = len(youtubeInfList_data['data'])
                    item.update({'no_of_influencers':no_of_youtube_influencers})
                    item.update({'youtube_inf_data': youtubeInfList_data['data']})
                except Exception as e:
                    print(e)
            print('campaign data', view_campaign_data)
            now = datetime.datetime.now()
            today_date = now.strftime("%d-%b-%y")
            print('today is ',today_date)
            print('today is ', type(today_date))
            for item in view_campaign_data['data']:
                print(type(item['from_date']))
                from_date = datetime.datetime.strptime(str(item['from_date']), '%d-%b-%y')
                print('from date =',from_date)
                to_date = datetime.datetime.strptime(str(item['to_date']), '%d-%b-%y')
                print('to date =', to_date)
                todays_date = datetime.datetime.strptime(str(today_date), '%d-%b-%y')
                print('todays date =', todays_date)
                if  from_date <= todays_date <= to_date :
                    print('i m between')
                    if item['campaign_status'] == 'InActive':
                       print(item['campaign_status'])
                    elif item['campaign_status'] == 'Finished':
                       print(item['campaign_status'])
                    elif item['campaign_status'] == 'New':
                       res = requests.put(url=self.url_update_campaign_status+'/'+str(item['campaign_id'])+'/'+'Active')
                    elif item['campaign_status'] == 'Queued':
                       res = requests.put(url=self.url_update_campaign_status+'/'+str(item['campaign_id'])+'/'+'Active')

                elif todays_date >= to_date :
                    print('i m expired')
                    if item['campaign_status'] == 'InActive' :
                       print(item['campaign_status'])
                    elif item['campaign_status'] == 'New':
                       print(item['campaign_status'])
                       res = requests.put(url=self.url_update_campaign_status + '/' + str(item['campaign_id']) + '/' + 'Finished')
                    elif item['campaign_status'] == 'Queued':
                       print(item['campaign_status'])
                       res = requests.put(url=self.url_update_campaign_status + '/' + str(item['campaign_id']) + '/' + 'Finished')
                    elif item['campaign_status'] == 'Active':
                       print(item['campaign_status'])
                       res = requests.put(url=self.url_update_campaign_status + '/' + str(item['campaign_id']) + '/' + 'Finished')

            return view_campaign_data
        except Exception as e:
            print(e)
            pass
            return view_campaign_data

    def get_campaign_details(self):
        view_campaign_details = ''
        try:
            view_campaign_details_response = requests.get(url=self.url_view_campaign_details)
            view_campaign_details = view_campaign_details_response.json()
            print(view_campaign_details)

            for item in view_campaign_details['data']:
                # print(item)
                region_id_list = item['regions'].split(',')
                region_name_list = []
                for region_id in region_id_list:
                    try:
                        region_name_response = requests.get(url=base_url + 'Youtube/regionCode/' + str(region_id))
                        region_data = region_name_response.json()
                        region_name = region_data['data'][0][1]
                        region_name_list.append(region_name)
                    except:
                        pass
                cat_response = requests.get(url=base_url + 'Youtube/videoCategories/' + str(item['video_cat_id']))
                # print(cat_response.json())
                cat_json_data = cat_response.json()
                video_cat_name = cat_json_data['data'][0]['video_cat_name']
                item.update({'video_cat_name': video_cat_name})
                item.update({'region_name_list': region_name_list})
                try:
                    string_from_date = datetime.datetime.strptime(item['from_date'], '%Y-%m-%d')
                    string_from_date = string_from_date.strftime('%d-%b-%y')
                    string_to_date = datetime.datetime.strptime(item['to_date'], '%Y-%m-%d')
                    string_to_date = string_to_date.strftime('%d-%b-%y')
                    item.update({'from_date': string_from_date})
                    item.update({'to_date': string_to_date})
                except Exception as e:
                    print(e)

                try:
                    youtubeInfListResponse = requests.get(url=self.url_getYoutubeInfList+str(item['campaign_id']))
                    youtubeInfList_data = youtubeInfListResponse.json()
                    no_of_youtube_influencers = len(youtubeInfList_data['data'])
                    item.update({'no_of_influencers':no_of_youtube_influencers})
                    item.update({'youtube_inf_data':youtubeInfList_data['data']})
                except Exception as e:
                    print(e)
            print('campaign details data', view_campaign_details)
            return view_campaign_details
        except Exception as e:
            print(e)
            pass
            return view_campaign_details



