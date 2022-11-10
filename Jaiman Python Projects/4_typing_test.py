from time import sleep, time
from random import choice

text_options = ["The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal: Ding. A single lap should be completed each time you hear this sound: Ding. Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, ding.",
                "A teacher's professional duties may extend beyond formal teaching. Outside of the classroom teachers may accompany students on field trips, supervise study halls, help with the organization of school functions, and serve as supervisors for extracurricular activities. In some education systems, teachers may have responsibility for student discipline",
                "The first personnel management department started at the National Cash Register Co. in 1900. The owner, John Henry Patterson, organized a personnel department to deal with grievances, discharges and safety, and training for supervisors on new laws and practices after several strikes and employee lockouts. During the 1970s, companies experienced globalization, deregulation, and rapid technological change which caused the major companies to enhance their strategic planning and focus on ways to promote organizational effectiveness. This resulted in developing more jobs and opportunities for people to show their skills which were directed to effective applying employees toward the fulfillment of individual, group, and organizational goals. Many years later the major/minor of human resource management was created at universities and colleges also known as business administration.",
                "There are many idiosyncratic typing styles in between novice-style 'hunt and peck' and touch typing. For example, many 'hunt and peck' typists have the keyboard layout memorized and are able to type while focusing their gaze on the screen. Some use just two fingers, while others use 3-6 fingers. Some use their fingers very consistently, with the same finger being used to type the same character every time, while others vary the way they use their fingers.",
                "The basic technique stands in contrast to hunt and peck typing in which the typist keeps his or her eyes on the source copy at all times. Touch typing also involves the use of the home row method, where typists keep their wrists up, rather than resting them on a desk or keyboard (which can cause carpal tunnel syndrome). To avoid this, typists should sit up tall, leaning slightly forward from the waist, place their feet flat on the floor in front of them with one foot slightly in front of the other, and keep their elbows close to their sides with forearms slanted slightly upward to the keyboard; fingers should be curved slightly and rest on the home row.",
                "A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs. Similar to desktop keyboards and input devices, if a user overuses keys which need hard presses and/or have small and unergonomic layouts, it could cause thumb tendonitis or other repetitive strain injury. (Wikipedia)",
                "Medical transcription, also known as MT, is an allied health profession dealing with the process of transcribing voice-recorded medical reports that are dictated by physicians, nurses and other healthcare practitioners. Medical reports can be voice files, notes taken during a lecture, or other spoken material. These are dictated over the phone or uploaded digitally via the Internet or through smart phone apps.",
                "Business casual is an ambiguously defined dress code that has been adopted by many professional and white-collar workplaces in Western countries. It entails neat yet casual attire and is generally more casual than informal attire but more formal than casual or smart casual attire. Casual Fridays preceded widespread acceptance of business casual attire in many offices."]
                
text = choice(text_options)

print('Type the following as accurately as you can.')
sleep(1)
print('Type "stop" as your last word to grade what you typed so far:\n')
sleep(1.5)

start = time()
user_input = input(f'{text}\n')
end = time()
text = text.lower()
text = text.split()
user_input = user_input.lower()
user_input = user_input.split()

wrong_words = 0
end_input = False
total_length = len(text)
for i in range(len(user_input)):
    if user_input[i] == text[i]:
        continue
    elif user_input[i] == 'stop' or user_input[i] == 'stop.':
        end_input = True
        total_length = i
        break
    else:
        wrong_words += 1
if not end_input:        
    if len(user_input) < len(text):
        wrong_words += len(text) - len(user_input)

words_right = total_length - wrong_words
accuracy = round(((words_right/total_length)*100), 2)
time_taken = round(end-start, 1)

print(f'You typed {total_length} words in {time_taken} seconds.')
print(f'You got {words_right}/{total_length} words right, which is {accuracy}% accuracy.')
