def save_new_words(words):
    with open('new_words.txt', 'a') as file:
        for word in words:
            file.write(word + '\n')

def chat_bot():
    print("سلام! من یک ربات گفتگو هستم.")
    print("برای خروج، 'exit' را بزنید.")

    # مجموعه‌ای برای ذخیره کلمات جدید
    new_words = set()

    # بارگذاری کلمات قبلی از فایل
    with open('new_words.txt', 'r') as file:
        for line in file:
            new_words.add(line.strip())

    while True:
        user_input = input("شما: ")

        if user_input.lower() == 'exit':
            print("خدانگهدار!")
            break
        else:
            # جدا کردن کلمات و بررسی برای کلمات تکراری
            words = user_input.split()
            new_unique_words = set(words) - new_words  # کلمات جدید تکراری نیستند
            if new_unique_words:
                new_words.update(new_unique_words)  # افزودن کلمات جدید به مجموعه

            # نمایش پاسخ
            response = "من فهمیدم!"
            print("ربات:", response)

    # ذخیره کلمات جدید در فایل
    save_new_words(new_unique_words)

if __name__ == "__main__":
    chat_bot()
