__author__ = 'handwa'

from urllib import parse, request
import json

client_id = '7e951996e3c2cc7b7d64'
client_secret = 'fed16a1234dc41c06ac045e7316d7684cfa8e460'
app_password = '4bd888ce59c9e74ab4caba6c30452bcf'
username = 'DaNiAnBot'
url = "https://online-go.com/api/v1/"

class OGSession:
    header = { # we will use urlencode to create our messages.
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    session_key = ''
    refresh_key = ''
    def __init__(self):
        # begin by setting up a post request to get the session_key
        values_list = [('client_id', client_id), ('client_secret', client_secret), ('grant_type', 'password'),
                       ('username', username), ('password', app_password)]
        body_dict = self.send_msg('https://online-go.com/oauth2/access_token', 'POST', values_list)
        self.session_key = body_dict["access_token"]
        self.refresh_key = body_dict["refresh_token"]
        # add the session key to the header
        self.header['Authorization'] = 'Bearer ' + self.session_key

    def me(self):
        new_url = url + "me/"
        body_dict = self.send_msg(new_url, 'GET')
        return body_dict

    # def acceptAllFriendRequests(self):
    #     req = request.Request(url + "me/friends/invitations/", headers=self.header)
    #     request_body = request.urlopen(req).read()
    #     str_body = request_body.decode('utf-8')
    #     body_dict = json.loads(str_body)
    #     print(body_dict)

    def list_challenges(self):
        new_url = url + "me/challenges/"
        body_dict = self.send_msg(new_url, 'GET')
        return body_dict

    def list_challenge_ids(self):
        new_url = url + "me/challenges/"
        body_dict = self.send_msg(new_url, 'GET')
        ret = [x['id'] for x in body_dict['results']]
        return ret

    def accept_challenge(self, id):
        new_url = url + "me/challenges/" + str(id) + "/accept/"
        body_dict = self.send_msg(new_url, 'POST')
        return body_dict;

    def delete_challenge(self, id):
        new_url = url + "me/challenges/" + str(id) + "/"
        body_dict = self.send_msg(new_url, 'DELETE')
        return body_dict

    def make_move(self, game, move):
        new_url = url + "games/" + str(game) + "/move/"
        values_list = [('move', move)]
        ret = self.send_msg(new_url, 'POST', values_list)
        return ret

    def get_sgf(self, game):
        new_url = url + "games/" + str(game) + "/sgf/"
        ret = self.send_msg_spec(new_url, 'GET')
        return ret

    def send_msg(self, url, method, values_list=[]):
        req = None
        if values_list != []:
            values_str = parse.urlencode(values_list)
            values_bytes = values_str.encode('utf-8')
            req = request.Request(url, data=values_bytes, headers=self.header)
        else:
            req = request.Request(url, headers=self.header)
        req.get_method = lambda: method
        request_body = request.urlopen(req).read()
        str_body = request_body.decode('utf-8')
        body_dict = json.loads(str_body)
        return body_dict;

    def send_msg_spec(self, url, method, values_list=[]):
        req = None
        if values_list != []:
            values_str = parse.urlencode(values_list)
            values_bytes = values_str.encode('utf-8')
            req = request.Request(url, data=values_bytes, headers=self.header)
        else:
            req = request.Request(url, headers=self.header)
        req.get_method = lambda: method
        request_body = request.urlopen(req).read()
        str_body = request_body.decode('utf-8')
        return str_body;

    # def refresh(self):
    #     values_list = [('client_id', client_id), ('client_secret', client_secret), ('grant_type', 'password'),
    #                    ('username', username), ('password', app_password)]
    #     values_str = parse.urlencode(values_list)
    #     values_bytes = values_str.encode('utf-8')
    #     req = request.Request('https://online-go.com/oauth2/access_token', data=values_bytes, headers=self.header)
    #     request_body = request.urlopen(req).read()
    #     print(request_body)
    #     self.header['Authorization'] = 'Bearer ' + self.session_key
