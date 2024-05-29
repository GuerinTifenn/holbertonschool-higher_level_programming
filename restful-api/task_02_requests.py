#!/usr/bin/python3
"""script to fetch posts from JSONPlaceholder using requests.get()"""
import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()
        posts_data = [{'id': post['id'], 'title': post['title'],
                       'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
