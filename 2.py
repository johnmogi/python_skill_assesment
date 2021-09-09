# total_speakers = 7539

# chinese_speakers = 1107
# english_speakers = 1121
# russian_speakers = 264.3

# chinese_speakers_share = chinese_speakers / total_speakers
# print("Share of people who speak Chinese:", chinese_speakers_share)

# english_speakers_share = english_speakers / total_speakers
# print("Share of people who speak English:", english_speakers_share)

# russian_speakers_share = russian_speakers / total_speakers
# print("Share of people who speak Russian:", russian_speakers_share)

chinese_native = 1107
print('Chinese is the native language for {} million people '.format(chinese_native))

total_speakers = 7539
chinese_speakers = 1107

chinese_speakers_share = chinese_speakers / total_speakers
print('Share of people who speak Chinese: {:.2}'.format(chinese_speakers_share))


total_speakers = 7539
chinese_speakers = 1107
english_speakers = 1121
russian_speakers = 264.3

chinese_speakers_share = chinese_speakers / total_speakers
english_speakers_share = english_speakers / total_speakers
russian_speakers_share = russian_speakers / total_speakers
print('Percentage of people who speak Chinese: {:.1%}'.format(chinese_speakers_share))
print('Percentage of people who speak English: {:.1%}'.format(english_speakers_share))
print('Percentage of people who speak Russian: {:.1%}'.format(russian_speakers_share))
