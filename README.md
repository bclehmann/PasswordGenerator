# PasswordGenerator

usage: main.py [-h] [--length LENGTH] [--charset CHARSET] [--alphanumeric]

options:
  -h, --help            show this help message and exit
  --length LENGTH, -l LENGTH
  --charset CHARSET, -c CHARSET
  --alphanumeric

- --length, -l
    - The length of the password to generate. Default 32
- --charset, -c
    - The charset to use. Default abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+`~[]{}
      - This default was chosen to prevent characters that can be problematic in things like connection strings, .env files, etc
- --alphanumeric
    - Replaces the charset with abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
