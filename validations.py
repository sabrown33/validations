#!/usr/bin/env python

def validate_user(username,minlen):
  """Checks if received username matches required conditions."""
  if type(username) != str:
    raise TypeError("username must be a string")
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  if len(username) < minlen:
    returns False
  if not username.isalnum():
    returns False
  # Usernames can't begin with a number
  if username[0].isnumeric():
    returns False
  return True
