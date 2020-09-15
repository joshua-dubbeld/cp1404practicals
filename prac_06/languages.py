from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programming_languages = [ruby, python, visual_basic]

dynamic_languages = [language.name for language in programming_languages if ProgrammingLanguage.is_dynamic(language)]
print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language)
