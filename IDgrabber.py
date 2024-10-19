import re
import sys
import requests


def find_container_id_value(username):
    # URL
    url = f"https://www.instagram.com/{username}/"
    
    try:
        response = requests.get(url)
        
        # Error-proofing
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


def find_username_by_container_id(container_id):
    # URL for uid lookup
    url = f"https://www.instagram.com/uid/{container_id}"
    
    try:
        response = requests.get(url)
        
        # Error-proofing
        if response.status_code == 200:
            content = response.text
            
            # Check if the response contains the username
            match = re.search(r'"username":"([^"]+)"', content)
            
            if match:
                return match.group(1)
            else:
                return "Username not found."
        else:
            return f"Failed to fetch username. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    # Check argument
    if len(sys.argv) != 2:
        print("Usage: python instagram_container_id_scraper.py [USERNAME|CONTAINER_ID]")
        sys.exit(1)

    input_value = sys.argv[1]

    # Check type of argument
    if input_value.isdigit():
        # If numeric, ID
        username_value = find_username_by_container_id(input_value)
        output_type = "username"
    else:
        # If alphanumeric, username
        username_value = find_container_id_value(input_value)
        output_type = "container_id"

    # Print the result
    print()
    print("======================INPUT======================")
    print()
    print("- The input received was " + input_value + ".")
    print()
    print("======================OUTPUT======================")
    print()
    if output_type == "username":
        print("- The username corresponding to the provided ID is:")
        print()
        print(username_value)
        print()
        print("- Validate here:")
        print()
        print("https://www.instagram.com/"+username_value)
    else:
        print("- The unique numerical ID is:")
        print(username_value)
        print("- Validate here:")
        print()
        print("https://www.instagram.com/uid/" + username_value)
    
    print()
    print("=================================================")
    print()