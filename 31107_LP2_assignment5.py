
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you ?", ]
    ],
    
    [
        r"hi|hey|hello",
        ["Hello, what's your name?"]
    ],
    [
        r"what is your name?",
        ["I am just a bot. But since I am being made for healthcare related work you can call me Healthbot!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?", ]
    ],

    [
        r"How can you help me?",
        ["What do you want to do?\n1. Healthcare centres in Pune\n2. Covid Vaccine centres in Pune\n Please enter one or two ", ]
    ],
    [
        r"I need some help",
        ["I can help you in the following.\n What do you want to do?\n1. Healthcare centres in Pune\n2. Covid Vaccine centres in Pune\n Please enter one or two ", ]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?", ]
    ],

    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?", ]
    ],
    [
        r"How can you help me?",
        ["What do you want to do?\n1. Healthcare centres in Pune\n2. Covid Vaccine centres in Pune\n Please enter one or two ", ]
    ],
    [
        r"I want to search healthcare centers",
        ["What do you want to do?\nA. Healthcare centres in Pune\nB. Covid Vaccine centres in Pune\n Please enter A or B", ]
    ],

    [
        r"A",
        ["Here is the list:\n 1. Deenanath Mangeshkar Hospital and Research Center\n2. Lokmanya Hospital\n3. Lotus Multispeciality Hospital\n4. Multispeciality Hospitals\n Please enter the number shown above", ]
    ],
    [
        r"1",
        ["Here are the details:\nContact: 020 4015 1000\nAddress: Mhatre Bridge, Erandwane, Pune, Maharashtra 411004\nTime: 24*7" ]
    ],
    [
        r"2",
        ["Here are the details:\nContact: 020-24424042\nAddress: 484/6, Mitramandal Colony Araneshwar road, Parvati, Pune 411 009.\nTime: 24*7 " ,]
    ],
    [
        r"3",
        ["Here are the details:\nContact: 084118 11558\nAddress: Dwarka Sai Wonders, Commercial Complex Survey no 173, Shiv Sai Road, Pimple Saudagar, Pune, Maharashtra 411027\nTime: 24*7", ]
    ],
    [
        r"4",
        ["Some of the Multispeciality Hospitals in Pune are as follows:\n1. Phoenix Hospital\n2. Punawale Multispecialioty Hospital\n3. Lifecare Multispeciality Hospital\n4. 7 Orange Hospitals",]
    ],
    
    [
        r"B",
        ["Here's the list of Covid Centers you can visit:\n1. Aundh E.S.I.C Hospital\n2. Jehangir Hospital\n3. Kamla Nehru Hospital\n4. Sahyadri Hospital"]
    ],
    

    [
        r"Thank You!",
        ["Is there anything I can help you?"]
    ],
    [
        r"yes",
         ["Here is the list:\n 1. Deenanath Mangeshkar Hospital and Research Center\n2. Lokmanya Hospital\n3. Lotus Multispeciality Hospital\n4. Multispeciality Hospitals\n Please enter the number shown above", ]
    ],
    [
        r"quit",
        ["Bye take care. Thank you!"]
    ],
    [
        r"no",
        ["Bye take care. Thank you!"]
    ],
    [
        r"",
        ["Sorry! I didn't catch that.\n Here is the costumer care number: 1234567890"]
    ],

]

reflections = {
  "i am": "you are",
  "i was": "you were",
  "i": "you",
  "i'm": "you are",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "my": "your",
  "you are": "I am",
  "you were": "I was",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me",
  "me": "you"
}

chat = Chat(pairs, reflections)
chat.converse()
