"""
Jackson Beadle
January 19, 2024
Take Home Assessment
Data Engineer -- Cribl

Question 3 -- API Interaction

Assumptions:

- API takes a 'page' parameter, will return empty response if page param is beyond total number of pages
- data returned as JSON object (all string keys/values) with minimum structure:

    { "items": [
        {"title": value,
         "author": value,
         "publication_date": value,
         "genre": value,
         "isbn": value
        }
    ]}

"""

import requests
import time
import argparse
import json


def fetch_book_data(url, page=1):
    """Function for reading book data from API.

    :param url: API URL
    :type url: str
    :param page: Starting page to read data from (default: 1)
    :type page: int
    :return: List of books with title, author, publication_date, genre, isbn
    :rtype: list(dict)
    """

    books = []
    max_retries = 10
    retry_delay = 1

    try:
        retries = 0
        while True:
            params = {'page': page}
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                if not data:
                    break  # no more data, exit the loop
                # parse response, add books to list

                for i in data['items']:
                    books.append({'title': i['title'],
                                  'author': i['author'],
                                  'publication_date': i['publication_date'],
                                  'genre': i['genre'],
                                  'isbn': i['isbn']})

            elif 400 <= response.status_code < 500:
                # client errors, do not retry
                print(f'Error: {response.status_code}  - {response.text}')
                break
            elif retries < max_retries:
                # retry with exponential backoff
                retries += 1
                total_delay = retry_delay * (2 ** retries)
                print(f'Retrying in {total_delay} seconds...')
                time.sleep(total_delay)
            else:
                print(f'Max retries reached... Error: {response.status_code} - {response.text}')
                break

    except Exception as e:
        print(f'Error occurred: {e}')
        return None

    return books


def parse_args():
    """Function to read optional runtime parameters for input and output file paths.

    :return: Runtime arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input_file', help='Name of input file containing partial book data', default=None)
    parser.add_argument('-o', '--output', dest='output_file', help='Name of output file to store JSON results', default=None)
    args, unknown = parser.parse_known_args()
    return args


def main():
    """Main function. If provided:
        - will read existing (partial) book data from JSON file to minimize data consumption from API
        - will write book data to JSON file for storage
    """

    api_url = 'https://example-api.com/books'
    args = parse_args()

    # if input file provided, read existing data
    if args.input_file:
        with open(args.input_file, 'r') as f:
            existing_books = json.loads(f.read())
        f.close()

        # get number of completely loaded pages
        loaded_pages = int(len(existing_books)/50)

        # load remaining data
        book_data = existing_books[:loaded_pages*50] + fetch_book_data(api_url, loaded_pages + 1)

    # otherwise start reading data from page 1
    else:
        book_data = fetch_book_data(api_url)

    # if output file is provided, write results
    if args.output_file and book_data:
        with open(args.output_file, 'w') as f:
            f.write(json.dumps(book_data))

    # otherwise pretty print to stdout
    elif book_data:
        print(json.dumps(book_data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
