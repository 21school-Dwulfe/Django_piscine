#!/usr/bin/env python3
import requests
import sys
import json
import dewiki


def wiki_request(query:str)->str:

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "parse",
        "page": query,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }
    response = requests.get(url=URL, params=PARAMS)
    response.raise_for_status()
    data = json.loads(response.text)
    if data.get("error") is not None:
        raise RuntimeError("{} {}".format(response.status_code, data["error"]["info"]))
    return (dewiki.from_string(data["parse"]['wikitext']['*']))

def main():
    if len(sys.argv) != 2:
       raise RuntimeError("Wrong number of arguments. Required one argument")
    request = wiki_request(sys.argv[1])
    print(request)
    with open("%s.wiki"%(sys.argv[1].strip().replace(' ', '_')), 'w') as output:
        output.write(request)
    
if  __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
            exit(1)

