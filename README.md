# 📂 File Organizer Script (Python)

A powerful and automated file organization tool built in Python that scans a directory and sorts files into categorized folders based on their file extensions.

This project was developed as part of an internship task to demonstrate practical skills in file handling, automation, and scripting.

---

## 🚀 Features

* 📁 Automatically organizes files into categories:

  * Images, Videos, Documents, Audio, Archives, Executables, Data, Others
* 🔁 Handles file name collisions (no overwriting)
* 🧪 Dry-run mode (preview changes before applying)
* 🕒 Scheduling support (run at a specific time)
* 📝 Logging system (tracks all operations in a log file)
* ⚡ Efficient and easy-to-use CLI interface

---

## 🛠️ Technologies Used

* Python 3
* Built-in Libraries:

  * `os` – directory and file handling
  * `shutil` – file moving operations
  * `datetime` – time handling and scheduling
  * `time` – delay for scheduler loop
  * `logging` – tracking operations

---

## 📦 How It Works

1. The script scans a selected directory
2. It checks each file’s extension
3. Files are moved into corresponding category folders
4. If a file with the same name exists:

   * It automatically renames the new file (e.g., `file_1.txt`)
5. Actions are logged into a `.log` file
6. Optional:

   * Run instantly or schedule for later
   * Preview actions using dry-run mode

---

## 🧪 Dry Run Mode

Dry run mode allows you to **preview what the script will do without actually moving files**.

Example output:

```text
[DRY RUN] Move: C:/Downloads/file.pdf -> C:/Downloads/Documents/file.pdf
```

✔ No files are changed
✔ Useful for testing and safety

---

## 🕒 Scheduling

You can schedule the script to run at a specific time (24-hour format).

Example:

```text
Enter time: 14:30
```

The script will continuously check the time and execute when it matches.

---

## 🔁 File Collision Handling

If a file already exists in the destination folder:

```text
file.txt → file_1.txt → file_2.txt
```

✔ Prevents overwriting
✔ Ensures all files are preserved

---

## 📝 Logging

All actions are recorded in:

```text
file_organizer.log
```

Example log:

```text
2026-04-28 14:30:01 - INFO - Moved: file.pdf -> Documents/file.pdf
2026-04-28 14:30:02 - INFO - [DRY RUN] Would move: image.png -> Images/image.png
```

✔ Tracks file movements
✔ Helps with debugging
✔ Provides execution history

---

## 📂 Project Structure

```text
file-organizer/
│── main.py
│── file_organizer.log
│── README.md
```

---

## ⚠️ Notes

* Ensure the directory path entered is valid
* Avoid running on system-critical folders
* Scheduler checks time every 30 seconds

---

## 👨‍💻 Author

This projrct was developed by **Emmanuel Joshua Deoduth**

---

## 📄 License

This project is for educational purposes as part of an internship program.

---
