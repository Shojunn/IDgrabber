from art import tprint
import re
import sys
import requests


#banner
tprint("ID Grabber")
print()

def find_container_id_value(username):
    #URL
    url = f"https://www.instagram.com/{username}/"
    
    try:
        response = requests.get(url)
        
        #Error-proofing
        if response.status_code == 200:
            content = response.text

            match = re.search(r'"container_id":"(\d+)"', content)
            
            if match:
                return match.group(1)
            else:
                return "container_id not found."
        else:
            return f"Failed to fetch page source. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Check
    if len(sys.argv) != 2:
        print("Usage: python instagram_container_id_scraper.py [USERNAME]")
        sys.exit(1)

    username = sys.argv[1]
    container_id_value = find_container_id_value(username)

    # Print the result

    print("===============INPUT===============")
    print()
    print("The input received was " + username + ".")
    print()
    print("===============OUTPUT===============")
    print()
    print("The unique numerical ID is:")
    print()
    print("- " + container_id_value)
    print()
    print("Validate here:")
    print()
    print("https://www.instagram.com/uid/"+container_id_value)
    print()
    print("===================================")
    print()