from random import choice

questions = ["Why is the sky blue?: ", "Why do stars twinkle?: ", "Where are the dinosaurs?: "]



question = choice (questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer =input ("Why?: ").strip().lower()

print ("Oh....Okay")
