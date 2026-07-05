import random
import string
import os
import sys
from playwright.sync_api import sync_playwright

def generate_random_string(length=6):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    url = "https://protoiptv.com/2026-iptvtrial-free-pro/"
    random_part = generate_random_string(6)
    
    email_address = f"bgdrtg+{random_part}@outlook.sa"
    name = f"Ismail_{generate_random_string(4)}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()
        
        try:
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(4000) 
            
            print(f"Email: {email_address}")
            page.locator('[name="wpforms[fields][1]"]').fill(name)
            page.locator('[name="wpforms[fields][2]"]').fill(email_address)
            
            country_field = page.locator('[name="wpforms[fields][34]"]')
            if country_field.count() > 0:
                country_field.select_option(label="Saudi Arabia")
            
            page.locator('[name="wpforms[fields][14]"][value="All Playlist"]').check()
            page.locator('[name="wpforms[fields][24]"][value="Yes"]').check()
            page.locator('[name="wpforms[fields][23]"]').fill("Please send the complete package.")
            
            print("Sending request...")
            submit_btn = page.locator('button[type="submit"], .wpforms-submit')
            submit_btn.first.click()
            page.wait_for_timeout(5000)
            print("Success")
            
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
