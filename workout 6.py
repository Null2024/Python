def is_palindrome(text):
    # حذف فاصله‌ها از ابتدا و انتهای رشته
    text = text.replace(" ", "")
    
    # تبدیل رشته به حروف کوچک
    text = text.lower()
    
    # بررسی آیا رشته برابر با ورودی خودش در بر عبارت است
    if text == text[::-1]:
        return True
    else:
        return False

print (is_palindrome("mmd"))
#کمک از - chatgpt