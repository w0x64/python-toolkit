import subprocess
from datetime import datetime
import os
from docx import Document

# AppleScript to fetch the latest email from Outlook for Mac
applescript = '''
tell application "Microsoft Outlook"
    try
        set theInbox to inbox
        set theMessages to messages of theInbox
        if (count of theMessages) > 0 then
            set theLatestMessage to item 1 of theMessages
            set messageSubject to subject of theLatestMessage
            set messageSender to sender of theLatestMessage
            set messageSenderName to name of messageSender
            set messageSenderAddress to address of messageSender
            set messageBody to content of theLatestMessage
            -- Return each part separately for debugging
            return "Subject: " & messageSubject & "\nSender: " & messageSenderName & " <" & messageSenderAddress & ">\nBody: " & messageBody
        else
            return "No messages in inbox."
        end if
    on error errMsg
        return "Error: " & errMsg
    end try
end tell
'''

# Execute AppleScript and capture the result
def run_applescript(script):
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE)
    result, _ = process.communicate()
    return result.decode('utf-8').strip()  # Make sure to strip any excess spaces/newlines

# Get the email details
output = run_applescript(applescript)

# Print the output to debug
print("AppleScript Output:\n", output)

# If the output is valid, proceed
if output != "No messages in inbox." and "Error:" not in output:
    # If the output has a recognizable format, split it
    if "Subject:" in output and "Sender:" in output and "Body:" in output:
        parts = output.split('\n')
        subject = parts[0].replace("Subject: ", "")
        sender = parts[1].replace("Sender: ", "")
        body = parts[2].replace("Body: ", "")
        
        # Prepare the content to be saved in the Word document
        content = f"Subject: {subject}\nSender: {sender}\n\n{body}"

        # Path for the new Word document on the desktop
        desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
        file_name = f"Latest_Email_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.docx"
        file_path = os.path.join(desktop, file_name)

        # Create a new Word document and add the content
        doc = Document()
        doc.add_paragraph(content)

        # Save the document on the desktop
        doc.save(file_path)

        print(f"Email has been saved as '{file_name}' on your Desktop.")
    else:
        print("AppleScript output is not in the expected format. Unable to parse subject, sender, and body.")
else:
    print(f"AppleScript returned an error or no messages: {output}")
