import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print(f"Error: Template should be a string, but got {type(template).__name__}.")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Attendees should be a list of dictionaries.")
        return
    
    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Define the placeholders we are looking for
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with corresponding values or "N/A" if missing
        processed_template = template[:]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A") or "N/A"
            processed_template = processed_template.replace(f"{{{placeholder}}}", value)
        
        # Generate the output file name
        output_filename = f"output_{idx}.txt"
        
        # Write the processed template to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        print(f"Generated: {output_filename}")

# Example usage
if __name__ == "__main__":
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: Template file not found.")
        template_content = ""
    
    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    
    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
