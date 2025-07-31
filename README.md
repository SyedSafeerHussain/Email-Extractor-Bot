# 📧 Email Extractor Bot

An intelligent automation tool that extracts email addresses from your Gmail inbox — both from the sender's address and within the message body. Designed for freelancers, marketers, and automation enthusiasts who need to gather contact data from incoming emails effortlessly.

---

## 🚀 Features

* 🔐 Secure IMAP login using environment variables
* 📬 Fetch emails from your Gmail inbox with custom date filters
* 📅 Supports filtering by date (e.g., fetch only emails before July 2024)
* 🧠 Extracts email addresses from:

  * Sender field
  * Message body (using regular expressions)
* 📤 Exports all collected emails to a structured CSV file
* 🧩 Modular code structure (services, utils, exporters)
* 🧪 Ready for unit testing and production use

---

## 📦 Project Structure

```
Email_Extractor/
│
├── config/               # Load environment variables
│   └── config.py
│
├── services/             # Handles IMAP connection and email fetching
│   └── imap_client.py
│
├── utils/                # Email parsing logic
│   └── email_parser.py
│
├── exporters/            # CSV saving logic
│   └── csv_exporter.py
│
├── .env                  # Contains your credentials (NOT committed)
├── main.py               # Entry point
└── README.md             # You’re reading it!
```

---

## ⚙️ Technologies Used

| Tool/Library   | Purpose                          |
| -------------- | -------------------------------- |
| `imap-tools`   | Connect to Gmail via IMAP        |
| `dotenv`       | Securely load environment values |
| `re` (Regex)   | Extract emails from message body |
| `csv`          | Export results to file           |
| `Python 3.10+` | Language                         |

---

## 🧑‍💻 How It Works

1. Connects to Gmail securely using your **app password**
2. Fetches emails (you can limit by number or date)
3. Parses each email to find addresses in:

   * `From` field
   * Email body
4. Filters out duplicates
5. Saves all clean email addresses to a `.csv` file

---

## 🛠️ Setup Instructions

**1. Clone the repo**

```bash
git clone https://github.com/yourusername/email-extractor-bot.git
cd email-extractor-bot
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your environment**
Create a `.env` file:

```
EMAIL=youremail@gmail.com
PASSWORD=yourapppassword
FOLDER=INBOX
```

**5. Run the bot**

```bash
python main.py
```

---

## 📈 Sample Output (CSV Format)

| Email Address                                       |
| --------------------------------------------------- |
| [john.doe@example.com](mailto:john.doe@example.com) |
| [contact@domain.org](mailto:contact@domain.org)     |
| [support@gmail.com](mailto:support@gmail.com)       |

---

## 💡 Use Cases

* 📬 Extracting contact info from job applications
* 📢 Building targeted email lists from inquiries
* 🤖 Automating lead generation

---

## 🔐 Security Note

* Your `.env` file is **excluded** from version control.
* Never share your credentials in public repositories.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## ✨ Author

**Safeer Hussain**
👨‍💻 Computer Science Student | Automation Enthusiast
