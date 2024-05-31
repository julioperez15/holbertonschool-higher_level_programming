#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    # Send a GET request to the JSONPlaceholder API for posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Parse the response JSON content
        posts = response.json()
        
        # Iterate over each post and print the title
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    # Send a GET request to the JSONPlaceholder API for posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        # Parse the response JSON content
        posts = response.json()
        
        # Prepare the list of dictionaries to write into CSV
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Define the CSV file name
        csv_file = "posts.csv"
        
        # Write the data into CSV using csv.DictWriter
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
        
        print(f"Data has been written to {csv_file}")
    else:
        print("Failed to fetch posts")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
