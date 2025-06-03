# Importing required modules
import socket
import threading
from datetime import datetime
import re
from autocorrect import Speller
from tkinter import messagebox
import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from pushbullet import Pushbullet
import time

API_KEY ="o.BJqRa9xD25pmXbrF02JdQte79uvNZL88"
# message = "Namaste"

# def display_message(message,client):
#     time.sleep(message['duration'])
#     dismessage = "~ Message disappeared"
#     client.sendall(dismessage.encode())
    # with conn.cursor() as cursor:
    #     cursor.execute("UPDATE chat SET message = %s WHERE sender = %s AND message = %s", (dismessage, message['username'], message['original_message']))
    #     conn.commit()

# def send_message(text, duration,client):
#     message = {'text': text, 'duration': duration}
#     threading.Thread(target=display_message, args=(message,client)).start()

# Example usage
# send_message("This message will disappear in 5 seconds", 5)




conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres123",
    host="localhost"
)

def ensure_tables_exist():
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usern (
                UID SERIAL PRIMARY KEY,
                USERNAME TEXT,
                EMAIL TEXT,
                EPASSWORD TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat (
                MID SERIAL PRIMARY KEY,
                SENDER TEXT,
                MESSAGE TEXT,
                TIMESTAMP TIMESTAMP
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS current_room (
                MID SERIAL PRIMARY KEY,
                USERNAME TEXT
            );
        """)
        conn.commit()
        print("✅ Database tables ensured.")



HOST = '127.0.0.1'
PORT = 1234 #We can use any port b/w 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] #List of all connected clients
date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

#Function to listen for messages from a client
def listen_for_messages(client, username):
    
    while 1:
        message = client.recv(2048).decode('utf-8')
        message = process_message(message)
        spell = Speller()

        if message  != '':
            
            final_msg = username + '~' + "  " +  spell(message) + "   " + date_now
            sqlmessage = '~' + "  " + spell(message)
            
            with conn.cursor() as cursor:
              cursor.execute("SELECT MAX(MID) FROM chat")
              current_id = cursor.fetchone()[0]
              if current_id is None:
                  current_id = 0
              next_id = current_id + 1
                   
              cursor.execute("INSERT INTO chat (MID,SENDER,MESSAGE,TIMESTAMP) VALUES ('%d','%s','%s','%s')" %(next_id,username,sqlmessage, date_now))
              conn.commit()
            send_messages_to_all(final_msg)
            # receive_file(filename, PORT)
            
        else:
            pass
            
            
def process_message(newmessage):
    # Define filtering rules
    profanity_filter = re.compile(r'\b(?:saala|fuck|arya)\b', re.IGNORECASE)  
    filtered_message = profanity_filter.sub('****',newmessage)
    return filtered_message        
    
# Function to send a message to a single client       
        
def send_message_to_client(client, message):
    client.sendall(message.encode())
    
    # send_email(message)
    
    # send_notification(message)
    
    
#Functio to send any new message to all the clients that are currently connected to the server
def send_messages_to_all(message):
     # Declare active_messages as a global variable
    for user in active_clients:
        send_message_to_client(user[1], message) 
    

#Function to handle client
def client_handler(client):
    
    # Server will listen for client message that will contain the username
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            with conn.cursor() as cursor:
                cursor.execute("SELECT (sender,message,timestamp) FROM chat WHERE sender  = ('%s') ORDER BY timestamp ASC" %(username))
                chat_history = cursor.fetchall()
                print(chat_history)
                formatted_messages = [format_message(msg[0]) for msg in chat_history]
                print(formatted_messages)
            active_clients.append((username,client))
            for message in formatted_messages:
                send_message_to_client(client, str(message))
                # send_message(message,10,client)# Assuming each message is converted to string
                
            break
            
        else:
            print("Client username is empty")
    threading.Thread(target=listen_for_messages, args=(client, username, )).start()
    
def format_message(input_string):
    # Split the input string into parts
    parts = input_string.strip("()").split(",")
    
    # Extract name, message, and timestamp
    name = parts[0].strip('()').split(',')[0].strip('"')
    message = "~ " + parts[1].strip('"~ ') 
    timestamp = "     " + parts[2].strip('"')
    
    # Format the message
    formatted_message = f"{name} {message} {timestamp}"
    
    return formatted_message
def send_email(message):
    me = "wildwhispers12@gmail.com"
    you = "leoadvait12@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "New Message"
    msg['From'] = me
    msg['To'] = you
    msg.set_content(message)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("wildwhispers12@gmail.com", "qkoy lnqv pozt qysa")
    server.send_message(msg)
    server.quit()
    
# def send_notification(message):
#     pb = Pushbullet(API_KEY)
#     push = pb.push_note("New Message",message) 

# Main function
def main():
    # Creating the socket class object
    # AF_INET: Means we're using IPv4 addresses
    # SOCK_STREAM: Means we're using TCP Protocol
    ensure_tables_exist() 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Creating a try catch block
    try:
        # Provide the server with an address in the form of HOST IP and Port
        server.bind((HOST,PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print("Unable to bind to host {HOST} and port {PORT}")
    
    # Set server limit
    server.listen(LISTENER_LIMIT)
    
    # This while loop will keep listening to client connection
    while 1:
        
        client, address = server.accept()
        print(f"Succesfully connected to client {address[0]} {address[1]}")        
        
        threading.Thread(target=client_handler, args=(client, )).start()
        # receive_file(filename, PORT) 

        
        
            
if __name__ == '__main__':
    main()