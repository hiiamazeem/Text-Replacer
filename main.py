user_input = input("Give me Text......\n")
print("Yup!")
replace_word = input("Tell me which Word You want to Replace\n")
count_word = user_input.count(replace_word)
print(
  f"OK I have scanned your text your text has {count_word} time {replace_word}"
)
new_word=input(f"Tell me new word for {replace_word}\n")
print("I am going to replace that ☺\n")
final_text=user_input.replace(replace_word,new_word)
print(final_text)
