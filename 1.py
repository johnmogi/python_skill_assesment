total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_share = 0.017
chinese_web_popularity = total_speakers / chinese_speakers

english_speakers = 1121
english_web_share = 0.539

russian_speakers = 264.3
russian_web_share = 0.061

print(f"""
--- Chinese ---
Share of speakers: {chinese_speakers} %
Share of websites in the language: {chinese_web_share} %
Web popularity index: {chinese_web_popularity}
""")